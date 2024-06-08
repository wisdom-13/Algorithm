from heapq import *
import sys
input = sys.stdin.readline


# 최대값이 기호 1번보다 작으면 리턴
N = int(input().rstrip())

votes1 = int(input().rstrip())
votes_list = []
cnt = 0

if N == 1:
    print(0)
    sys.exit()

for i in range(N - 1):
    votes_list.append(-int(input().rstrip()))

heapify(votes_list)

while -votes_list[0] >= votes1:
    votes_max = heappop(votes_list)
    heappush(votes_list, votes_max + 1)
    cnt += 1
    votes1 += 1

print(cnt)
