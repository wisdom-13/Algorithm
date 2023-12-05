function solution(absolutes, signs) {
    var answer = 0;
    
    for (i in absolutes) {
        answer += Number(absolutes[i]) * Number(signs[i] ? 1 : -1)
    }
    
    return answer;
}