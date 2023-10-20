function solution(players, callings) {
    var playerMap = {}
    
    for (let i = 0; i < players.length; i++) {
        playerMap[players[i]] = i;
    }
    
    
    for (i in callings) {
        var index = Number(playerMap[callings[i]])
        var tmp = players[index - 1];
        
        playerMap[players[index]] = index - 1;
        playerMap[tmp] = index; 
        
        players[index - 1] = players[index];
        players[index] = tmp;
    }
    
    return players;
}