import sys
input = sys.stdin.readline


N, K = map(int, input().rstrip().split())
coin_list = [int(input().rstrip()) for _ in range(N)][::-1]
money, cnt = K, 0

for coin in coin_list:
    if coin > K:
        continue

    if (money // coin >= 1):
        cnt += money // coin
        money %= coin

    if money == 0:
        break


print(cnt)