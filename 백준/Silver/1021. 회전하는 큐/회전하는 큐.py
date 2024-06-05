from collections import deque
import sys
input = sys.stdin.readline

size, num = map(int, input().rstrip().split())
target_arr = list(map(int, input().rstrip().split()))

queue = deque(range(1, size + 1))
cnt = 0

for target in target_arr:
    # 1. target의 위치 찾기
    target_index = queue.index(target)

    # 왼쪽으로 돌릴경우
    if (target_index <= len(queue) // 2):
        cnt += target_index
        queue.rotate(target_index * -1)

    # 오른쪽으로 돌릴경우
    else:
        cnt += len(queue) - target_index
        queue.rotate(len(queue) - target_index)

    queue.popleft()


print(cnt)
