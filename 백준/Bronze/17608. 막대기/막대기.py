from collections import deque
import sys
input = sys.stdin.readline


num = int(input().rstrip())
list = [int(input().rstrip()) for _ in range(num)]
max, cnt = 0, 0

for i in list[::-1]:
    if i > max:
        cnt += 1
        max = i

print(cnt)
