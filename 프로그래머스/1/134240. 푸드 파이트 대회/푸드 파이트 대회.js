function solution(food) {
    var answer = '';
    
    food = food.splice(1);
    food = food.map((item) => ~~(item / 2));
    
    for (i in food) {
        answer += ((Number(i)+1)+'').repeat(food[i])
    }
    
    return answer += ('0' + [...answer].reverse().join(''))
    
}