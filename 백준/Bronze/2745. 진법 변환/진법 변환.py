import sys
input = sys.stdin.readline

d = {}
# 1. A-Z까지 대응하는 숫자를 저장 (아스키코드 A는 65)
for i in range(36):
    if (i <= 9):
        d[str(i)] = i
    else:
        d[chr(55 + i)] = i

N, B = input().rstrip().split()

# 2. 각 자리수의 문자를 숫자로 변환한 값 * B의 (각자리수)제곱
num = 0
intB = int(B)
length = len(N)

for i in range(length):
    num += d[str(N[i])] * (intB ** (length - i - 1))

print(num)
