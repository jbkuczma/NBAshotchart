function goToPlayerPage(player){
	var id = (player[12] === null ? 'None' : player[12]);
	var url = '/player/' + id;
	window.location = url;
}