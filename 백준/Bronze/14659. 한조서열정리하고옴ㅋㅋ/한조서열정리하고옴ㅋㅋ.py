import sys
input = sys.stdin.readline


N = int(input().rstrip())
archer_list = list(map(int, input().rstrip().split()))
score = 0
height = archer_list[0]
cnt = 0

for i in range(1, N):
    if archer_list[i] < height:
        cnt += 1
    else:
        height = archer_list[i]
        score = max(score, cnt)
        cnt = 0


print(max(score, cnt))
