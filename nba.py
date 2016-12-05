import requests
import json
from random import randint

class NBA():

	def __init__(self, teamID):
		self.teamList = self.getTeams()
		self.team = teamID or self.getRandomTeam()
		self.season = "2016-17" # has to be manually changed for every season

	def makeRequest(self, url):
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
		r = requests.get(url=url, headers=headers)
		if r.status_code == 400:
			print('NBA we have a problem')
		response = r.text
		return json.loads(response)

	def getTeams(self):
		teams = []
		with open('teams.txt') as f:
			for line in f:
				teams.append(line.strip())
		return teams

	def getRandomTeam(self):
		return self.teamList[randint(0, len(self.teamList)-1)]

	def getTeam(self):
		url = 'http://stats.nba.com/stats/teaminfocommon?LeagueID=00&SeasonType=Regular+Season&TeamID={}&season={}'.format(self.team, self.season)
		data = self.makeRequest(url)
		city = data['resultSets'][0]['rowSet'][0][2]
		nickname = data['resultSets'][0]['rowSet'][0][3]
		return  city + ' ' + nickname

	def getRoster(self):
		url = 'http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season={}&TeamID={}'.format(self.season, self.team)
		data = self.makeRequest(url)
		return data["resultSets"][0]["rowSet"]