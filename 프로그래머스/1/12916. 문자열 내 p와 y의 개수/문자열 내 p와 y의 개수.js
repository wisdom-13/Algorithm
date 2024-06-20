function solution(s){
    s = s.toLowerCase()
    
    let p_cnt = s.split('p').length;    
    let y_cnt = s.split('y').length;
    
    return p_cnt == y_cnt;
}