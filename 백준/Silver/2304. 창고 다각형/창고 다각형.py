from heapq import *
import sys
input = sys.stdin.readline


# 1. 중앙 기둥을 기준으로 오른쪽과 왼쪽 영역으로 나눔
# 2. 각 영역을 각각의 끝에서부터 시작하면서 이전 기둥보다 높으면 높은 기둥 값 + 낮으면 이전 기둥값 +
def get_area(start, end, step):
    cnt, max_now = 0, 0
    for s in range(start, end, step):
        max_now = max(max_now, pillar.get(s, max_now))
        cnt += max_now
    return cnt


N = int(input().rstrip())
pillar = {}
max_l, max_h = 0, 0  # 가장 높은 기둥의 위치와 높이
start, end = 1000, 0  # 좌표의 시작값과 끝값
cnt = 0

for i in range(N):
    L, H = map(int, input().rstrip().split())

    if max_h < H:
        max_l, max_h = L, H

    start = min(start, L)
    end = max(end, L)
    pillar[L] = H

total_area = max_h
total_area += get_area(start, max_l, 1)
total_area += get_area(end, max_l, -1)

print(total_area)
