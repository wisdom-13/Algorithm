from collections import deque
import sys
input = sys.stdin.readline

case = int(input().rstrip())

for i in range(case):
    queue = deque()
    num, item_index = map(int, input().rstrip().split())

    # 1. 튜플 형태로 index와 우선순위 저장
    queue = deque((v, i)
                  for i, v in enumerate(map(int, input().rstrip().split())))

    cnt = 0

    # 2. queue가 빌때까지 반복
    while len(queue) > 0:
        cnt += 1

        # lambda x: x[0] : 튜플의 첫 번째 요소를 반환
        max_index = max(enumerate(queue), key=lambda x: x[1][0])[0]

        queue.rotate(max_index * -1)

        if queue[0][1] == item_index:
            break

        queue.popleft()

    print(cnt)
