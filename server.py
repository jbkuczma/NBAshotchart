from flask import Flask, current_app, render_template
import os
from nba import NBA, Player

# setting where to look at html template
templateDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(
		__name__, 
		template_folder = templateDirectory
	  )

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/team/<teamID>')
def team(teamID):
	nba = NBA(teamID=teamID)
	# team = nba.getTeam()
	roster = nba.getRoster()
	# return current_app.send_static_file('index.html', result=result)
	return render_template('team.html', roster=roster, team=nba.team, teamName=nba.getTeam())

# where the actual shot chart will be
@app.route('/player/<playerID>')
def player(playerID):
	# render the shot chart on server and display 
	player = Player(playerID)
	shotChart = player.getShotData()
	# we have the data
	return render_template('player.html', playerID=playerID, shotChart=shotChart)