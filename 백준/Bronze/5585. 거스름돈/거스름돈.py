import sys
input = sys.stdin.readline


coins = [500, 100,  50, 10, 5, 1]
cnt = 0
price = 1000 - int(input().rstrip())


for coin in coins:
    cnt += price // coin  # 사용한 동전 개수
    price = price % coin  # 남은 잔돈

    if price == 0:
        break

print(cnt)
