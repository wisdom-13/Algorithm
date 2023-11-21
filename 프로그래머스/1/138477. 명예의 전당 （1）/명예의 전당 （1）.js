function solution(k, score) {
    var answer = [];
    var arr = [];
    
    for (i in score) {
        if (i < k) {
            arr.push(score[i]);
        } else if (score[i] > Math.min(...arr)) {
            arr[arr.indexOf(Math.min(...arr))] = score[i]
        }
        
        answer.push(Math.min(...arr))
    }
    
    return answer;
}