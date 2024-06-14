import sys
input = sys.stdin.readline


N = int(input().rstrip())
score = []
cnt = 0

for i in range(N):
    score.append(int(input().rstrip()))

# 점수 리스트를 정렬해서 index와 예상점수의 차를 저장
for entry in enumerate(sorted(score)):
    i, v = entry
    cnt += abs((i+1) - v)

print(cnt)
