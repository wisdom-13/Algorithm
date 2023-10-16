function solution(common) {
    var answer = 0;
    var plusArr = [];
    var divideArr = [];
    
    for (i in common) {
        if (i > 0) {
            plusArr.push(common[i] - common[i-1])
            divideArr.push(common[i] / common[i-1]) 
        }
        
    }
    
    plusArr = [...new Set(plusArr)]
    divideArr = [...new Set(divideArr)]

    
    if (plusArr.length == 1) {
        return common[common.length - 1] + Number(plusArr.join('')) 
    } else if (divideArr.length == 1) {
        return common[common.length - 1] * Number(divideArr.join('')) 
    }
    
}