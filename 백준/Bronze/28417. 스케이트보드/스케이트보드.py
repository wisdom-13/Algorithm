import sys
input = sys.stdin.readline

N = int(input().rstrip())

score_list = []

for i in range(N):
    score = list(map(int, input().rstrip().split()))
    a_score = max(score[0:2])
    b_score = sum(sorted(score[2:], reverse=True)[0:2])

    score_list.append(a_score + b_score)

print(max(score_list))
