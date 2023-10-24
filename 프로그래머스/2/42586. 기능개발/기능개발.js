function solution(progresses, speeds) {
    var answer = [];
    var wait = [];
    
    for (i = 0; i < progresses.length; i++) {
        var day = Math.ceil((100 - progresses[i]) / speeds[i]);
        wait.push(day)
    }
    
    var tmp = 0
    for (j = 0; j < wait.length; j++) {
        if (j == 0 || tmp < wait[j] ) {
            tmp = wait[j]
            answer.push(1)
        } else {
            answer[answer.length - 1] = answer[answer.length - 1] + 1
        }
    }
    
    return answer;
}