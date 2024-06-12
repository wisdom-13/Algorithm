from itertools import permutations
import sys
input = sys.stdin.readline


K, L = map(int, input().rstrip().split())
result = ''


# # L이 소인수라면 나눈것의 몫 보다 크면 BAD
if K % L == 0 and K // L < L:
    result = K // L

# 소인수가 아니라면 값을 줄여가면서 체크, 있으면 BAD
elif K % L != 0:
    for i in range(L, 2, -1):
        if K % i == 0:
            result = min(i, K // i)
            break

if result:
    print("BAD", result)
else:
    print("GOOD")
