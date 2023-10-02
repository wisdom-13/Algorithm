function solution(babbling) {
    var answer = 0;
    var arr = ['aya', 'ye', 'woo', 'ma'];
    
    for (i in babbling) {
        var a = babbling[i]
        for (j in arr) {
            
            a.split(arr[j])
        }
        return a
    }
    
    return answer;
}