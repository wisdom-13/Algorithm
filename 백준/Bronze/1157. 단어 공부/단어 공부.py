
from collections import Counter
w = str(input()).upper() 

# 1. Counter : 문자열에서 각각의 글자가 몇번 사용되는지 
# 2. most_common : 사용 빈도 순으로 튜틀 형태로 정렬 해줌  
# ex) [('I', 4), ('S', 4), ('M', 1), ('P', 1)]

t = Counter(w).most_common() 
mode = t[0][0]

# 3. 튜플에 첫번째와 두번째의 빈도 수가 같다면 ? 출력

if (len(t) > 1 and t[0][1] == t[1][1]):
    print('?')
else:
    print(mode)
