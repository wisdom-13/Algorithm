function solution(num, total) {
    var answer = [];
    var n = (Math.ceil(num/2) - 1) * -1
    
    for (i=0; i<num; i++) {
        answer.push(~~(total/num) + n)
        n += 1
    }
    
    return answer;
}