from itertools import permutations
import sys
input = sys.stdin.readline


# 최소 값 조건 : 112233과 같이 동일한 숫자가 붙어있어야 함 > 123의 순열 개수 출력
N = int(input().rstrip())
perm_list = set(permutations(list(range(1, N+1))))

print(len(perm_list))
