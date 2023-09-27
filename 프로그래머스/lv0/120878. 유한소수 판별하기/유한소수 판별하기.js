function solution(a, b) {
    
    var answer = 0;
    
    const gcd = ((a, b) => a % b === 0 ? b : gcd(b, a % b));

    answer = prime(b / gcd(a,b)).filter((item) => item != 2 && item != 5)
    
    return answer.length > 0 ? 2 : 1;
}


function prime(n) {
  let result = [];
  let divisor = 2;
  
  while (n >= 2) {
    if (n % divisor === 0) {
      result.push(divisor)
      n = n / divisor;
    }
     else divisor ++;
  }
  
  return [...new Set(result)];
}