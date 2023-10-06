function solution(id_pw, db) {
    var answer = 'fail';
    
    for (i in db) {
        if (db[i][0] == id_pw[0]) {
            answer = 'wrong pw';
            if (db[i][1] == id_pw[1]) {
                answer = 'login';
            }
        }
    }
    
    return answer;
}