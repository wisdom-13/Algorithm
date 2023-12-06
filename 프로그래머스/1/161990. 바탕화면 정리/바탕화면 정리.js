function solution(wallpaper) {
    var answer = [0, 0, 0, 0];
    var arr = [];
    var arrX = [];
    var arrY = [];
    
    for (i in wallpaper) {
        arr.push(wallpaper[i].split(''))
    }
    
    for (var i = 0; i < wallpaper.length; i++) {
        for (var j = 0; j < wallpaper[0].length; j++) {
            if (arr[i][j] == "#") {
                arrX.push(j);
                arrY.push(i);
            }
        }
    }
    
    answer = [
        Math.min(...arrY), 
        Math.min(...arrX), 
        Math.max(...arrY) + 1,
        Math.max(...arrX) + 1
    ]
    
    return answer;
}