import sys
input = sys.stdin.readline


# 이전 2개를 만드는데 필요한 방법의 합
def dp(n):
    memo = [0, 1, 2]
    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]


N = int(input().rstrip())
print(dp(N) % 10007)