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
	for player in roster:
		if player[11] == None:
			player[11] = 'None'
	# return current_app.send_static_file('index.html', result=result)
	return render_template('team.html', roster=roster, team=nba.team, teamName=nba.getTeam())

# where the actual shot chart will be
@app.route('/player/<playerID>')
def player(playerID):

	player = Player(playerID)
	shotChart = player.getShotData()
	headers = shotChart['resultSets'][0]['headers']
	shots = shotChart['resultSets'][0]['rowSet']

	# print(shots)
	# print('---')

	grapher = Grapher(shots)
	x,y,shotStatus = grapher.getShotCoordinates()

	# split shot coordinates into made and miss
	madeX = []
	madeY = []
	missedX = []
	missedY = []
	for i in range(len(x)):
		if shotStatus[i] == 'Made Shot':
			madeX.append(x[i])
			madeY.append(y[i])
		else:
			missedX.append(x[i])
			missedY.append(y[i])

	file = grapher.makeGraph(x,y, madeX, madeY, missedX, missedY)

	return render_template('player.html', playerID=playerID, shotChart=file)

@app.after_request
def addHeader(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response