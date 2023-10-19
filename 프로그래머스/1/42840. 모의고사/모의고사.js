function solution(answers) {
    var answer = [];
    var num = [];
    
    var a = "12345".repeat(Math.ceil(answers.length / 5));
    var b = "21232425".repeat(Math.ceil(answers.length / 8));
    var c = "3311224455".repeat(Math.ceil(answers.length / 10));
    
    num[0] = answers.filter((item, index) => item == a[index]).length
    num[1] = answers.filter((item, index) => item == b[index]).length
    num[2] = answers.filter((item, index) => item == c[index]).length
    
    for (i in num) {
        if (num[i] == Math.max(...num)) {
            answer.push(Number(i)+1)
        }
    }
    
    return answer;
}