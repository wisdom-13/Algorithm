import sys
input = sys.stdin.readline


def dp(n):
    memo = [0, 0, 0, 1, 0, 1]  # 방법이 없으면 0 / 3과 5에 1로 초기화
    for i in range(6, n+1):

        memo.append(0)

        # 3또는 5을 뺏을 때 값이 있다면 성립 / 뺀 값에 +1
        if memo[i-5] > 0:
            memo[i] += memo[i-5] + 1

        elif memo[i-3] > 0:
            memo[i] += memo[i-3] + 1

        elif memo[i-3] == 0 and memo[i-5] == 0:
            memo[i] = 0

    return memo[n]


N = int(input().rstrip())
num = dp(N)
print(num if num != 0 else -1)