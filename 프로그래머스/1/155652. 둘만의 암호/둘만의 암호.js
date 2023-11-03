function solution(s, skip, index) {
    const alpabet = [..."abcdefghijklmnopqrstuvwxyz"].filter((item) => !skip.includes(item))
    return [...s].map((item) => alpabet[(alpabet.indexOf(item) + index)%alpabet.length]).join('')
    
}