function solution(array) {
    var count = {};
    array.map((v) => count[v] ? count[v] += 1 : count[v] = 1);
    
    var max = Number(Object.keys(count).reduce((a, b) => count[a] > count[b] ? a : b));
    var chk = Object.values(count).filter((e) => e == count[max]).length > 1 ? -1 : max;
    
    return chk;
}