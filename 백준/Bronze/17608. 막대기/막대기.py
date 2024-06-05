import sys
input = sys.stdin.readline


num = int(input().rstrip())
list = [int(input().rstrip()) for _ in range(num)]
max, cnt = 0, 0

# 1. 배열을 뒤집어서 max 값과 비교, 더 크다면 max를 변경하고 cnt를 1 증가
for i in list[::-1]:
    if i > max:
        cnt += 1
        max = i

print(cnt)