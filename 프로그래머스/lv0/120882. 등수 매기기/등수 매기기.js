function solution(score) {
    var answer = [];
    var rank = [];
    
    score = score.map((item) => item.reduce((a, b) => a + b) / 2);
    rank = [...score].sort((a, b) => b - a)
    
    return score.map((item) => rank.indexOf(item) + 1)
    
}