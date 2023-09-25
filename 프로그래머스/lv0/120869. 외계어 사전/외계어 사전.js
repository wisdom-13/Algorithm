function solution(spell, dic) {
    var answer = 2;
    for (i in dic) {
        const filter = [...dic[i]].filter((v) => spell.includes(v))
        if ([...new Set(filter)].length == spell.length) {
            answer = 1
        }
        
    }
    return answer;
}