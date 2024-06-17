from collections import deque
import sys
input = sys.stdin.readline


N = int(input().rstrip())
dist_list = deque(map(int, input().rstrip().split()))
price_list = deque(map(int, input().rstrip().split()))

min_price = price_list.popleft()  # 첫번째 도시의 가격
total_price = min_price * dist_list.popleft()  # 두번째 도시까지 가는 비용

while dist_list:
    min_price = min(price_list.popleft(), min_price)  # 최소 주유비와 현재 도시의 주유비 비교
    total_price += min_price * dist_list.popleft()  # 최소 가격 * 다음 도시까지 가는 비용

print(total_price)
