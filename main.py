from flask import Flask
import os
import challonge

# set creds:
MyKey = os.environ['MyKey']
# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
challonge.set_credentials("TheMightyPong", MyKey)


      

app = Flask(__name__)


@app.route('/')
def index():
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
  html = '<html><head>'
  html += '<link rel="stylesheet" type="text/css" href="/static/style.css">'
  html += '</head><body>'
  html += '<div class="match">'
  html += '<div class="player">' + P1Name + '</div>'
  html += '<div class="VersusText">' +' Vs.'
  html += '<div class="player">' + P2Name + '</div>'
  html += '</div>'
  html += '</body></html>'
    
  return html


app.run(host='0.0.0.0', port=81)
