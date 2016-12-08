function goToPlayerPage(player){
	// can't go to player page if None is found in player array
	var id = (player[player.length-1] === null ? 'None' : player[player.length-1]);
	var url = '/player/' + id + '?player='+ player;
	window.location = url;
}

function setProperties(url){
	playerDataString = decodeURI(url).split('?')[1].slice(7); // 7 comes from the 'player=' at the beginning
	playerData = playerDataString.split(',')
	console.log(playerData)


	document.getElementById('playerName').innerHTML = playerData[3];
	document.getElementById('playerNumPos').innerHTML = '#' + playerData[4] + ' | ' + playerData[5];
	document.getElementById('playerTitle').innerHTML = playerData[3];
}

function goBackToPlayerPage(){

}
function addTeams(){
	const teamList = [
		['Atlanta Hawks','1610612737'],
		['Brooklyn Nets','1610612751'],
		['Boston Celtics','1610612738'],
		['Charlotte Hornets','1610612766'],
		['Chicago Bulls','1610612741'],
		['Cleveland Cavaliers','1610612739'],
		['Dallas Mavericks','1610612742'],
		['Denver Nuggets','1610612743'],
		['Detroit Pistons','1610612765'],
		['Golden State Warriors','1610612744'],
		['Houston Rockets', '1610612745'],
		['Indiana Pacers','1610612754'],
		['Los Angeles Clippers','1610612746'],
		['Los Angeles Lakers','1610612747'],
		['Memphis Grizzlies','1610612763'],
		['Miami Heat','1610612748'],
		['Milwaukee Bucks','1610612749'],
		['Minnesota Timberwolves','1610612750'],
		['New Orleans Pelicans','1610612740'],
		['New York Knicks','1610612752'],
		['Oklahoma City Thunder','1610612760'],
		['Orlando Magic','1610612753'],
		['Philadelphia 76ers','1610612755'],
		['Phoenix Suns','1610612756'],
		['Portland Trailblazers','1610612757'],
		['Sacramento Kings','1610612758'],
		['San Antonio Spurs','1610612759'],
		['Toronto Raptors','1610612761'],
		['Utah Jazz','1610612762'],
		['Washington Wizards','1610612764']
	]
	var ul = document.getElementById("teams");
  	for(var i = 0; i < teamList.length; i++){
  		var link = document.createElement('a');
  		link.setAttribute('href', 'team/'+teamList[i][1]);
  		link.innerHTML = teamList[i][0];
  		var li = document.createElement("li");
  		//document.createTextNode(teamList[i])
  		li.appendChild(link);
  		ul.appendChild(li)
  	}
  	
}