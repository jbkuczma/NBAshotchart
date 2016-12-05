from flask import Flask, current_app, render_template
import os
from nba import NBA

# setting where to look at html template
templateDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(
		__name__, 
		template_folder = templateDirectory
	  )

@app.route('/')
def main():
	nba = NBA()
	team = nba.getTeam()
	roster = nba.getRoster()
	# return current_app.send_static_file('index.html', result=result)
	return render_template('index.html', roster=roster, team=team)

@app.route('/team/<teamID>')
def team(teamID):
	return teamID

# where the actual shot chart will be
@app.route('/player/<playerID>')
def player(playerID):
	return playerID