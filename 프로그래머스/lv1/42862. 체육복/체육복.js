function solution(n, lost, reserve) {
    var answer = n;
    
    var hap = lost.filter((i) => reserve.includes(i))
    
    lost = lost.filter((i) => !hap.includes(i)).sort((a, b) => a - b)
    reserve = reserve.filter((i) => !hap.includes(i)).sort((a, b) => a - b)
    
    
    for (i in lost) {
         if (reserve.includes(lost[i] - 1)) {
            removeItem(reserve, lost[i] - 1)
        } else if (reserve.includes(lost[i] + 1)) {
            removeItem(reserve, lost[i] + 1)
        } else {
            answer -= 1
        }
    }
    
    return answer;
}


function removeItem(arr, item) {
    return arr.splice(arr.indexOf(item), 1)
}
