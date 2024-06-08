from heapq import *
import sys
input = sys.stdin.readline


# k(k+1)/2가 num 보다 작아야함
def get_jump_count(num):
    low, high = 1, num

    while low <= high:
        mid = (low + high) // 2
        if mid * (mid + 1) // 2 <= num:
            low = mid + 1
        else:
            high = mid - 1

    return high


T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    print(get_jump_count(N))
