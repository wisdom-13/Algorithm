from heapq import *
import sys
input = sys.stdin.readline


# heapq에서 가장 작은 값 2개를 뽑아서 total에 +
# 2개를 더한 값을 다시 heapq에 저장
# heapq에 더할 값이 남아있지 않을때 까지 반복

def get_total_time(k_list):
    total = 0
    heapify(k_list)

    while len(k_list) > 1:
        a = heappop(k_list)
        b = heappop(k_list)

        total += (a + b)
        heappush(k_list, (a+b))

    return total


T = int(input().rstrip())
for i in range(T):
    K = int(input().rstrip())
    k_list = list(map(int, input().rstrip().split()))

    print(get_total_time(k_list))
