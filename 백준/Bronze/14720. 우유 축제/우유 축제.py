from collections import deque
import sys
input = sys.stdin.readline


N = int(input().rstrip())
milks = deque(map(int, input().rstrip().split()))

now_milk, drink_milk = 0, 0  # 이번에 마셔아하는 우유 / 마신 우유

while milks:
    milk = milks.popleft()
    if milk == now_milk:  # 마셔야할 우유와 같다면
        drink_milk += 1
        now_milk = (now_milk + 1) % 3

print(drink_milk)
