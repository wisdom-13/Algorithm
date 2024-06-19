function solution(arr) {
    let answer = 0;
    let prev_arr = conversion(arr)
    
    if (arr.toString() == prev_arr.toString()) {
        return answer
    }
    
    while (1 > 0) {
        arr = conversion(prev_arr)
        if (arr.toString() === prev_arr.toString()) {
            break
        }
        
        prev_arr = arr
        answer += 1
    }
    
    return answer + 1;
}

function conversion(arr) {
    return arr.map((v) => {
        if (v >= 50 && v % 2 == 0) {
            return v/2
        } else if (v < 50 && v % 2 == 1) {
            return v * 2 + 1
        } else {
            return v
        }
    })
}