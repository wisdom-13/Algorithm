function solution(n) {
    
    const max = (n*(n+1))/2;
    const answer =  Array(n).fill().map((_, i) => Array(i+1).fill(0));
    
    let [i, j, count] = [0, 0, 1];
    
    while(count <= max) {
        while (i < n && !answer[i][j]) {
            answer[i++][j] = count++;
        }
        
        i--, j++;
        
        while (j < n && !answer[i][j]) {
            answer[i][j++] = count++;
        }
        
        i--, j -= 2;
        
        while (i > 0 && j > 0 && !answer[i][j]) {
            answer[i--][j--] = count++;
        }
        
        i += 2, j++;
    }
    
    return answer.flat();
}