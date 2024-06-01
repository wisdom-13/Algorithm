from collections import Counter
import sys
input = sys.stdin.readline

text = sorted(input().rstrip())
new_text = ''
center = ''
error = False

# 1. 입력된 문자열의 요소의 종류 만큼 반복
counter = Counter(text)
for i in counter.items():

    # 2. 홀수개만큼 존재하는 글자가 2개 이상이라면 팰린드롬이 아님
    #    1개라면 센터값
    if i[1] % 2 == 1:
        if center == '':
            center = i[0]
        else:
            error = True
            break

    # 3. 입력된 개수의 /2 만큼 반복하여 새로운 문자열에 추가
    new_text += str(i[0])*int(i[1]/2)

# 4. 새로운 문자열 + 센터값 + 새로운 문자열의 역순
new_text = new_text+center+new_text[::-1]

print("I'm Sorry Hansoo" if error else new_text)