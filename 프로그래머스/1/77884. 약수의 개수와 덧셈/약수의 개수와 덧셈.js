function solution(left, right) {
    var answer = 0;
    
    for (i = left; i<=right; i++) {
        if (measure(i) % 2 !== 0) {
            answer += i
        } else {
            answer -= i
        }
    }
    
    return answer;
}
    
function measure(num) {
    var result = 0;
    
    for(i=0; i<num; i++) {
        if (num % i === 0) {
            result += 1;
        }
    }
    
    return result
}