function solution(lines) {
    let arr
    (arr = []).length = 200;
    arr.fill(0);
    
    for (i = 0; i<3; i++) {
        for (j = lines[i][0]; j < lines[i][1]; j++) {
            arr[j+100] += 1
        }
    }
    
 
    return arr.filter(v => v >= 2).length;
}