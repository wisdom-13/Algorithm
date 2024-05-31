import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 1. 1부터 n까지의 리스트 생성
# 2. combinations 함수를 사용하여 n개중에 m개를 고른 조합을 나열
arr = list(range(1, n + 1))
nCr = combinations(arr, m)

for combination in nCr:
    print(" ".join(map(str, combination)))
