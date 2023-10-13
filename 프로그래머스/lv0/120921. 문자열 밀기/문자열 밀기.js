function solution(A, B) {
    var answer = 0;
    var arrA = [...A]

    if (A == B) {
        return 0
    }
    
    for(i=0; i<A.length; i++) {
        answer += 1
        newArr = [arrA[arrA.length - 1], ...arrA]
        newArr.pop()
        
        arrA = newArr
        
        if (newArr.join('') == B) {
            return answer
        }
        
    }
    return -1;
}