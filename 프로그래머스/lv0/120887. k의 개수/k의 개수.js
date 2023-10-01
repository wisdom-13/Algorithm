function solution(i, j, k) {
    var answer = 0;
    
    for (a = i; a <= j; a++) {
        if ((a+'').includes(k)) {
            answer += (a+'').split(k).length - 1
        }
    }
    
    return answer;
}