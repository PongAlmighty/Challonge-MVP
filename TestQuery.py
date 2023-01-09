
# this page is not the most recent one. 
# Go here instead: https://replit.com/@TheMightyPong/Challonge-Query-Tester#main.py
# going to leave this here as a reference but otherwise, kinda pointless.







import challonge
# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).

# set creds:
MyKey = os.environ['MyKey']
challonge.set_credentials("TheMightyPong", MyKey)

# Get ALL the things!
tournament = challonge.tournaments.show('z57xc9')
participants = challonge.participants.index(tournament["id"])
matches = challonge.matches.index(tournament["id"])

# Tournaments, matches, and participants are all represented as normal Python dicts.
print(tournament["id"])  # 3272
print(tournament["name"])  # My Awesome Tournament
print(tournament["started-at"])  # None

# Retrieve the participants for a given tournament.
participants = challonge.participants.index(tournament["id"])
print(len(participants))  # 13

# Start the tournament and retrieve the updated information to see the effects
# of the change.

tournament = challonge.tournaments.show(tournament["id"])
print(tournament["started-at"])  # 2011-07-31 16:16:02-04:00
