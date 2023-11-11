function solution(k, m, score) {
    var answer = 0;
    var box = ~~(score.length / m);
    
    score = score.sort((a, b) => b - a);
    for (i = 0; i < box; i++) {
        answer += score[i * m + m - 1] * m;
    }
    
    return answer;
}