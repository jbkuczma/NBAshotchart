from flask import Flask, current_app, render_template
import os
from nba import NBA, Player
from grapher import Grapher

# setting where to look at html template
templateDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')

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

	player = Player(playerID)
	shotChart = player.getShotData()
	headers = shotChart['resultSets'][0]['headers']
	shots = shotChart['resultSets'][0]['rowSet']

	grapher = Grapher(shots)
	x,y,shotStatus = grapher.getShotCoordinates()
	file = grapher.makeGraph(x,y, shotStatus)

	return render_template('player.html', playerID=playerID, shotChart=file)

@app.after_request
def addHeader(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response