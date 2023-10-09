function solution(s) {
    var array = s.split(' ');
    var tmp = 0;
    var answer = 0;
    
    for (i in array) {
        if (array[i] !== 'Z') {
            tmp = array[i];
            answer += Number(array[i]);
        } else {
          answer -= Number(tmp);
        }
    }
    
    return answer;
}