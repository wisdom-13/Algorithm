function solution(s) {
    var answer = 0;
    var x = s[0];
    var xCount = 0;
    var notXCount = 0;
    
    for (i = 0; i < s.length; i++) {
        if (x == s[i]) {
            xCount += 1
        } else {
            notXCount += 1
        }
        
        if (xCount + notXCount != 0 && xCount == notXCount) {
            x = s[i+1];
            xCount = 0;
            notXCount = 0;
            answer += 1;
        } else if (i == s.length - 1) {
            answer += 1;
        }
    }
    
    return answer;
}