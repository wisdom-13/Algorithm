function solution(quiz) {
    
    let arr = [];
    
    quiz.map(v => {
        arr.push(chk(v))
    })
    
    return arr;
}

function chk(q) {
    var arr = q.split(' = ');
    return eval(arr[0]) == Number(arr[1]) ? "O" : "X"
    
}