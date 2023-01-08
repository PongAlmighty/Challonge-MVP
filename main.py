from flask import Flask, render_template
import os
import challonge
import time
from threading import Thread

# (http://api.challonge.com/v1). for Challonge docs

# set creds:
MyKey = os.environ['MyKey']
challonge.set_credentials("TheMightyPong", MyKey)

app = Flask(__name__)
# store the current state of the HTML page
current_html = ''

def update_html():
  global current_html
  try:
    P1Name = 'Player 1'
    P2Name = 'Player 2'
    
    # Retrieve a tournament by its id (or its url).
    tournament = challonge.tournaments.show('z57xc9')
    participants = challonge.participants.index(tournament["id"])
    matches = challonge.matches.index(tournament["id"])
    
    # get list of open matches
    for match in matches:
      if match["state"] == "open":
        if match["underway_at"] is not None:
          #print(match["id"])
          #print(match)
          Player1ID = int(match['player1_id'])
          Player2ID = int(match['player2_id'])
          #get player names
          Player1Info = challonge.participants.show(tournament["id"], Player1ID)
          Player1Name = Player1Info['name']
    
          Player2Info = challonge.participants.show(tournament["id"], Player2ID)
          Player2Name = Player2Info['name']
          P1Name=(Player1Name)
          P2Name=(Player2Name)
  
    # format the HTML output using CSS styles
    with app.app_context():
      new_html = render_template('index.html', P1Name=P1Name, P2Name=P2Name)
      
    # update the HTML page if the new HTML is different from the old HTML
    if new_html != current_html:
      current_html = new_html
      return current_html  # return the updated HTML
  except Exception as e:
    print(e)

def update_html_loop():    
# update the HTML page every 20 seconds
  while True:
    update_html()
    time.sleep(20)
  
# start the update loop in a separate thread
update_thread = Thread(target=update_html_loop)
update_thread.start()

# start the Flask app and run the development web server
@app.route('/')
def index():
  print('Accessed index route')
  return current_html

app.run(host='0.0.0.0', port=81)