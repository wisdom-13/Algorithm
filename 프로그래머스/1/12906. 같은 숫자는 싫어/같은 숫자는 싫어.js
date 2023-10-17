function solution(arr)
{
    var answer = [];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i+1] == arr[i]) { continue }
        answer.push(arr[i])
    }
    
    return answer;
}