function solution(keymap, targets) {
    var arr = {};
    
    keymap = keymap.map((item) => item.split(''))
    targets = targets.map((item) => item.split(''))
    
    for (i in keymap) {
        for (j in keymap[i]) {
            if (!arr[keymap[i][j]]) {
                arr[keymap[i][j]] = Number(j) + 1     
            
            } else if (arr[keymap[i][j]] > Number(j) + 1) {
                arr[keymap[i][j]] = Number(j) + 1    
            }
        }
    }
    
    return targets.map((item) => {
        return item.reduce((a, b) => {
            return (arr[b] && a != -1) ? a + arr[b] : -1
        }, 0)
    })
    
}