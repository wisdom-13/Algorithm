function solution(my_string) {
    var answer = 0;
    var arr = [...my_string];
    var tmp = '';
    
    for(i in arr) {
        if (!isNaN(arr[i])) {
            tmp += arr[i]
        } else if (tmp != '') {
            answer += Number(tmp)
            tmp = ''
        }
        
        if (i == arr.length - 1 && tmp != '') {
            answer += Number(tmp)
        }
        
    }
    
    return answer;
}