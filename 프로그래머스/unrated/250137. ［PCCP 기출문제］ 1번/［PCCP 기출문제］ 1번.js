function solution(bandage, health, attacks) {
    let hp = health;
    let attack = {};
    let stack = 0;
    
    let [time, recovery, bonus] = bandage;
    
    attacks.forEach(([time, damage]) => {
        attack[time] = damage;
    })
    
    
    
    for (i = 0; i<=attacks[attacks.length-1][0]; i++) {
    
        // 공격 o
        if (Object.keys(attack).includes(String(i))) {
            stack = 0;
            hp -= attack[i];
            
        // 공격 x
        } else {
            stack += 1;
            hp += recovery;
        }
        
        if (stack == time) {
            hp += bonus;
            stack = 0;
        }
        
        
        if (hp >= health) {
            hp = health;
        }
        
        if (hp <= 0) {
            return -1;
        }
        
        console.log(`시간:${i} 체력:${hp} 연속:${stack} `)
    }
    
    return hp;
}