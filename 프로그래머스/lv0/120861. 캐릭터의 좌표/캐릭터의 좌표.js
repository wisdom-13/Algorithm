function solution(keyinput, board) {
   
    var x = 0;
    var y = 0;
    
    var maxX = Math.floor(~~board[0]/2);
    var minX = Math.floor(~~board[0]/2) * -1;
    
    var maxY = Math.floor(~~board[1]/2);
    var minY = Math.floor(~~board[1]/2) * -1;
    
    for (i in keyinput) {
        switch(keyinput[i]) {
            case 'left':
            (x <= minX) ? x = minX : x -= 1
            break;
                
            case 'right':
            (x >= maxX) ? x = maxX : x += 1;
            break;
                
            case 'up':
            (y >= maxY) ? y = maxY : y += 1
            break;
                
            case 'down':
            (y <= minY) ? y = minY : y -= 1
            break;
            
        }
    }
    
    
    
    return [x, y];
}