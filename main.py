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

# Variables for the End User to fill out:
MyKey = os.environ['MyKey']
challonge.set_credentials("TheMightyPong", MyKey)
tournament = challonge.tournaments.show('z57xc9')
global updateTime # time in Seconds betweeen updates
updateTime = 5


app = Flask(__name__)
CORS(app)



participants = challonge.participants.index(tournament["id"])
matches = challonge.matches.index(tournament["id"])
data_updated = int(time.time())
last_update = tournament["updated_at"]

def index_html():
  return render_template('index.html')


def update_loop():
  global last_update, data_updated, torunament, participants, matches
  # update the Data every X seconds
  while True:
    try:
      print("refresh global var data")
      # Retrieve a tournament by its id (or its url).
      tournament = challonge.tournaments.show('z57xc9')
      participants = challonge.participants.index(tournament["id"])
      matches = challonge.matches.index(tournament["id"])

      # check if there has been any updates
      if tournament["updated_at"] > last_update:
        last_update = tournament["updated_at"]
        data_updated = int(time.time())
      for match in matches:
        if match["updated_at"] > last_update:
          last_update = match["updated_at"]
          data_updated = int(time.time())
        
      
    except Exception as e:
      print(e)
    time.sleep(updateTime)


# start the update loop in a separate thread
update_thread = Thread(target=update_loop)
update_thread.start()


# start the Flask app and run the development web server
@app.route('/')
def index():
  print('Accessed index')
  return index_html()

@app.route('/leaderboard')
def leaderout():
  print('Accessing Leaderboard index')
  return leaderboard.leaderboard(app, tournament, participants, matches)

@app.route('/leaderboard_data')
def leaderdataout():
  print('Updating Leaderboard data')
  return leaderboard.leaderboard_data(app, tournament, participants, matches)

@app.route('/leader_check')
def leader_check():
  global data_updated
  update_status = {'data_updated': data_updated}
  return jsonify(update_status)

@app.route('/versus')
def versusscreen():
  print('sending versus screen')
  return versus.versus(app, tournament, participants, matches)

@app.route('/versus_data')
def vdout():
  print('sending versus screen data')
  return versus.versus_data(app, tournament, participants, matches)

@app.route('/update_check')
def update_check():
  global data_updated
  update_status = {'data_updated': data_updated}
  return jsonify(update_status)


app.run(host='0.0.0.0')