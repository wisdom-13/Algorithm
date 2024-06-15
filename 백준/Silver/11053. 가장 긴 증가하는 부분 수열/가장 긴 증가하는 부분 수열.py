import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))