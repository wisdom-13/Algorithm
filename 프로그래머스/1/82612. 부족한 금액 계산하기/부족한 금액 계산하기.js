function solution(price, money, count) {
    var total = 0;
    
    for (i = 1; i <= count; i++) {
        total += i * price;        
    }

    return total - money > 0 ? total - money : 0;
}