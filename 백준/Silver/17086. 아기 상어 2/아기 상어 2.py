from collections import deque

# 상하좌우 대각선
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


def bfs(grid, N, M):
    # 초기화
    queue = deque()
    distance = [[-1] * M for _ in range(N)]

    # 모든 상어의 위치
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j))
                distance[i][j] = 0

    # BFS
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    # 가장 큰 거리
    max_distance = max(max(row) for row in distance)
    return max_distance


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(bfs(grid, N, M))
