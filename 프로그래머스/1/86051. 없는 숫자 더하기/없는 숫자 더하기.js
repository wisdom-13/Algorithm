function solution(numbers) {
    let num = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    num = num.filter((item) => !numbers.includes(item)).reduce((a, b) => a + b, 0);
    return num;
}