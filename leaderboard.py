from flask import render_template
import collections


def update_finished(app, tournament, participants, matches):
  try:

    # get list of open matches
    for match in matches:
      if match["state"] != "open":
        if match["underway_at"] is not None:
	      # Create a defaultdict to store the win/loss records for each participant
          records = collections.defaultdict(lambda: {"wins": 0, "losses": 0})

	      # Iterate through the list of matches and update the records for each participant
        for match in matches:
          player1_id = match["player1_id"]
          player2_id = match["player2_id"]
          winner_id = match["winner_id"]
          # Find the names of the players in this match
          player1_name = next((p["name"] for p in participants if p["id"] == player1_id), "Unknown")
          player2_name = next((p["name"] for p in participants if p["id"] == player2_id), "Unknown")
	        # Update the win/loss records for each player
          if winner_id == player1_id:
            # Player 1 won, so increment their win count and decrement player 2's loss count
            records[player1_name]["wins"] += 1
            records[player2_name]["losses"] += 1
          else:
            # Player 2 won, so increment their win count and decrement player 1's loss count
            records[player2_name]["wins"] += 1
            records[player1_name]["losses"] += 1

	       # Print out the win/loss records for each participant
	       #for participant, record in records.items():
	       #print(f"{participant}: {record['wins']} - {record['losses']} ")

	       # format the HTML output using CSS styles
        with app.app_context():
	         new_html = render_template('leaderboard.html', parent_list = records)

        return new_html  # return the updated HTML
      
  except Exception as e:
    print(e)
