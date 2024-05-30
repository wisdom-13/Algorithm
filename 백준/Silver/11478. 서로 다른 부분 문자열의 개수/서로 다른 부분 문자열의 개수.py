string = input()
s = []

# 1. 문자열의 길이만큼 반복
for i in range(1, len(string) + 1):

    # 2. 문자열 길이만큼 반복하면서, 한글자씩 옮겨가면서 i 길이만큼으로 문자열을 나눔
    s += [string[j:j+i] for j in range(len(string))]

# 3. set으로 중복을 제거한 후 길이 출력
print(len(set(s)))