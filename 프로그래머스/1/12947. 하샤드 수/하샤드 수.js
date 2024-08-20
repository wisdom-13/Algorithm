function solution(x) {
    
    return x % (x+'').split('').reduce((a,b) => a + Number(b), 0) ? false : true;
}