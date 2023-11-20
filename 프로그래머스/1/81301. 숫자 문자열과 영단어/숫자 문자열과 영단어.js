function solution(s) {
    var word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    word.map((item, i) => s = s.replaceAll(item, i))
    return Number(s);
}