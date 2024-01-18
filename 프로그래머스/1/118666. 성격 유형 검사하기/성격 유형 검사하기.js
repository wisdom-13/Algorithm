function solution(survey, choices) {
    var answer = '';
    var arr = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for (var i = 0; i<survey.length; i++) {
        var type = survey[i].split('')
        
        if (choices[i] < 4) {
            arr[type[0]] += 4 - choices[i]
            
        } else if (choices[i] > 4) {
            arr[type[1]] += choices[i] - 4
        }
    }
    
    answer += (arr['R'] >= arr['T']) ? 'R' : 'T';
    answer += (arr['C'] >= arr['F']) ? 'C' : 'F';
    answer += (arr['J'] >= arr['M']) ? 'J' : 'M';
    answer += (arr['A'] >= arr['N']) ? 'A' : 'N';

    return answer;
}