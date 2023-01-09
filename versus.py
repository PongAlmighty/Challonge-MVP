from flask import render_template
import challonge
import time

def versus(app, tournament, participants, matches):
  try:
    P1Name = 'Player 1'
    P2Name = 'Player 2'

    # get list of open matches
    for match in matches:
      if match["state"] == "open":
        if match["underway_at"] is not None:
          #print(match["id"])
          #print(match)
          Player1ID = int(match['player1_id'])
          Player2ID = int(match['player2_id'])
          #get player names
          Player1Info = challonge.participants.show(tournament["id"],
                                                    Player1ID)
          Player1Name = Player1Info['name']

          Player2Info = challonge.participants.show(tournament["id"],
                                                    Player2ID)
          Player2Name = Player2Info['name']
          P1Name = (Player1Name)
          P2Name = (Player2Name)

    # format the HTML output using CSS styles
    with app.app_context():
      new_html = render_template('versus.html', P1Name=P1Name, P2Name=P2Name, currenttime=int(time.time()))
      return new_html  # return the updated HTML
  except Exception as e:
    print(e)

def versus_data(app, tournament, participants, matches):
  try:
    P1Name = 'Player 1'
    P2Name = 'Player 2'

    # get list of open matches
    for match in matches:
      if match["state"] == "open":
        if match["underway_at"] is not None:
          #print(match["id"])
          #print(match)
          Player1ID = int(match['player1_id'])
          Player2ID = int(match['player2_id'])
          #get player names
          Player1Info = challonge.participants.show(tournament["id"],
                                                    Player1ID)
          Player1Name = Player1Info['name']

          Player2Info = challonge.participants.show(tournament["id"],
                                                    Player2ID)
          Player2Name = Player2Info['name']
          P1Name = (Player1Name)
          P2Name = (Player2Name)

    # format the HTML output using CSS styles
    with app.app_context():
      new_html = render_template('versus_data.html', P1Name=P1Name, P2Name=P2Name, currenttime=int(time.time()))
      return new_html  # return the updated HTML
  except Exception as e:
    print(e)



    