function solution(my_string) {
    var answer = my_string.split(/\D+/).reduce((a, b) => a + Number(b), 0)
    return answer;
}