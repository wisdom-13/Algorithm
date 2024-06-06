from heapq import *
import sys
input = sys.stdin.readline


N = int(input().rstrip())
heep = []
for _ in range(N):
    x = int(input().rstrip())
    if x:
        # 절대값과 기존 값을 튜플로 저장 (heap에 튜플 형식으로 추가하면 첫번째 값을 기준으로 정렬된다.)
        heappush(heep, (abs(x), x))
    else:
        if heep:
            print(heappop(heep)[1])
        else:
            print(0)
