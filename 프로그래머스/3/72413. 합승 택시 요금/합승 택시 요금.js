// 참고: 플로이드 와샬 알고리즘 

function solution(n, s, a, b, fares) {
    // 1. 빈 배열 만들기
    const map =  Array(n).fill().map(() => Array(n).fill(Infinity));
    
    // 2. x -> y 비용 배열에 저장 
    fares.forEach(([x, y, cost]) => {
        map[x-1][y-1] = cost;
        map[y-1][x-1] = cost;
    })
    for(let i = 0; i < n; i++) map[i][i] = 0;
    
    // 3. x -> y 최소값 저장
    for (let i = 0; i < n; i++) { // i : 거쳐가는 노드
        for (let j = 0; j < n; j++) { // j : 출발 노드
            for (let k = 0; k < n; k++) { // k : 도착 노드 
                map[j][k] = Math.min(map[j][k], map[j][i] + map[i][k]);
            }
        }
    }
    
    // 4. 합승구간 + A 혼자 + B 혼자 최소 값 계산
    var min = Infinity
    for (let point = 0; point < n; point++) {
        min = Math.min(map[s-1][point] + map[point][a-1] + map[point][b-1], min)
    }
    
    return min;
}