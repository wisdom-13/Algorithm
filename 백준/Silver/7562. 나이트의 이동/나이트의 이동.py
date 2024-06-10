import sys
from collections import deque

input = sys.stdin.readline

# 나이트의 이동 가능 위치


def moveable_pos(size, pos):
    x, y = pos
    pos = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2),
    ]

    # 이동 가능 위치중에 체스판을 넘어가는 것을 삭제하고 return
    return [(nx, ny) for nx, ny in pos if 0 <= nx < size and 0 <= ny < size]


def bfs(size, start, end):
    if start == end:
        return 0

    queue = deque([start])
    visited = [[-1] * size for _ in range(size)]
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for nx, ny in moveable_pos(size, (x, y)):
            if visited[nx][ny] == -1:  # 방문하지 않은 곳
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if (nx, ny) == end:
                    return visited[nx][ny]
    return -1


def knight_move_cnt():
    size = int(input().rstrip())
    startX, startY = map(int, input().rstrip().split())
    endX, endY = map(int, input().rstrip().split())

    result = bfs(size, (startX, startY), (endX, endY))
    print(result)


T = int(input().rstrip())
for _ in range(T):
    knight_move_cnt()
