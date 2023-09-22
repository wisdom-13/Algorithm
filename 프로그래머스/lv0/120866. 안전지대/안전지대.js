function solution(board) {
    var answer = 0
    
    for (i in board) {
        for (j in board[i]) {
            var mi = i == 0 ? 0 : Number(i) - 1 
            var pi = i == (board.length - 1) ? board.length - 1 : Number(i) + 1
            
            var mj = j == 0 ? 0 : Number(j) - 1 
            var pj = j == (board.length - 1) ? board.length - 1 : Number(j) + 1
            
            if (
                board[i][j] == 0
                && board[mi][mj] == 0
                && board[mi][j] == 0
                && board[mi][pj] == 0
                && board[i][mj] == 0
                && board[i][pj] == 0
                && board[pi][mj] == 0
                && board[pi][j] == 0
                && board[pi][pj] == 0
            ) {
                answer += 1;
            } 
        }
    }
    
    return answer;
}