function solution(sides) {
    var answer = 0;
    
    for (i = 0; i<Math.max(...sides); i++) {
        if (Math.max(...sides) <= i + Math.min(...sides)) {
            answer += 1;
        }
    }
    answer += (sides[0] + sides[1]) - Math.max(...sides) -1
    
    return answer;
}