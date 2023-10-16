function solution(nums) {
    var answer = 0;
    
    var max = nums.length/2
    var type = [...new Set(nums)].length
    
    return (max > type) ? type : max;
}