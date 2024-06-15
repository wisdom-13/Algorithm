import sys
input = sys.stdin.readline


# 이전 3개의 숫자를 만드는데 필요한 방법의 합
def dp(n):
    memo = [0, 1, 2, 4]
    for i in range(4, n+2):
        memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    return memo[n]


T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    print(dp(N))