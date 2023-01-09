from flask import Flask, render_template, jsonify
import os
import challonge
import time
from threading import Thread
from flask_cors import CORS
import collections
import versus
import leaderboard

# (http://api.challonge.com/v1). for Challonge docs

# set creds:
MyKey = os.environ['MyKey']
challonge.set_credentials("TheMightyPong", MyKey)

app = Flask(__name__)
CORS(app)
# store the current state of the HTML page
current_html = ''

data_updated = int(time.time())
tournament = challonge.tournaments.show('z57xc9')
participants = challonge.participants.index(tournament["id"])
matches = challonge.matches.index(tournament["id"])

def update_html():
  return render_template('index.html')


def update_html_loop():
  global current_html, data_updated
  # update the HTML page every 20 seconds
  while True:
    try:
      # Retrieve a tournament by its id (or its url).
      tournament = challonge.tournaments.show('z57xc9')
      participants = challonge.participants.index(tournament["id"])
      matches = challonge.matches.index(tournament["id"])

      
    except Exception as e:
      print(e)
    update_html()
    time.sleep(5)


# start the update loop in a separate thread
update_thread = Thread(target=update_html_loop)
update_thread.start()


# start the Flask app and run the development web server
@app.route('/')
def index():
  print('Accessed index route')
  return current_html

@app.route('/leaderboard')
def finishedout():
  print('Updating Leaderboard')
  return leaderboard.update_finished(app, tournament, participants, matches)

@app.route('/versus')
def versusscreen():
  print('sending versus screen')
  return versus.versus(app, tournament, participants, matches)

@app.route('/versus_data')
def vdout():
  print('sending versus screen data')
  return versus.versus_data(app, tournament, participants, matches)

@app.route('/update-check')
def update_check():
  global data_updated
  update_status = {'data_updated': data_updated}
  return jsonify(update_status)


app.run(host='0.0.0.0')