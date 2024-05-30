import sys
input = sys.stdin.readline

string = input().rstrip()
s = []

# 1. 문자열의 길이 - 1 만큼 반복
for i in range(1, len(string)):

    # 2. 문자열 길이만큼 반복하면서, 한글자씩 옮겨가면서 i 길이만큼으로 문자열을 나눔
    s += [string[j:j+i] for j in range(len(string))]

# 3. set으로 중복을 제거한 set의 길이 + 자기 자신의 개수
print(len(set(s)) + 1)
