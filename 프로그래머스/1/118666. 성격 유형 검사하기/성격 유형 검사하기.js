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
    
    if (arr['R'] >= arr['T']) {
        answer += 'R'
    } else {
        answer += 'T'
    }
    
    if (arr['C'] >= arr['F']) {
        answer += 'C'
    } else {
        answer += 'F'
    }
    
    if (arr['J'] >= arr['M']) {
        answer += 'J'
    } else {
        answer += 'M'
    }
    
    if (arr['A'] >= arr['N']) {
        answer += 'A'
    } else {
        answer += 'N'
    }
    
    

    return answer;
}