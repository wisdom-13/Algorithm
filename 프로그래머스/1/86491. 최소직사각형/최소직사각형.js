function solution(sizes) {
    var answer = 0;
    var x = 0;
    var y = 0;
    
    sizes = sizes.map((item) => item.sort((a, b) => a - b))
    
    for (i in sizes) {
        if (sizes[i][0] > x) { x = sizes[i][0] }
        if (sizes[i][1] > y) { y = sizes[i][1] }
    }
    
    return x*y;
}