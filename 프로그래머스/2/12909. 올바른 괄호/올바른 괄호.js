function solution(s){
    var tmp = 0
    
    for (i = 0; i < s.length; i++) {
        if (s[i] == "(") tmp += 1
        if (s[i] == ")") tmp -= 1
        if (tmp < 0) return false
    }
    
    return tmp == 0
}