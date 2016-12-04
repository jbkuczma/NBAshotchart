import requests
import json
from random import randint

class NBA():

	def __init__(self):
		self.teamList = self.getTeams()
		self.team = self.getRandomTeam()
		self.season = "2016-17" # has to be manually changed for every season

	def getTeams(self):
		teams = []
		with open('teams.txt') as f:
			for line in f:
				teams.append(line.strip())
		return teams

	def getRandomTeam(self):
		return self.teamList[randint(0, len(self.teamList)-1)]

	def getRoster(self):
		url = 'http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season={}&TeamID={}'.format(self.season, self.team)
		r = requests.get(url)
		if r.status_code == 400:
			print('NBA we have a problem')
		response = r.text
		data = json.loads(response)
		return data["resultSets"][0]["rowSet"]