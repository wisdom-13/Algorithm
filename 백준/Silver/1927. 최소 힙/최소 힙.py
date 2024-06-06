from heapq import *
import sys
input = sys.stdin.readline


N = int(input().rstrip())
heep = []
for _ in range(N):
    x = int(input().rstrip())
    if x:
        heappush(heep, x)
    else:
        if heep:
            print(heappop(heep))
        else:
            print(0)
