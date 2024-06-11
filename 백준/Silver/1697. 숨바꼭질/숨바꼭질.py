import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target):
    queue = deque([start])
    visited[start] = 0

    while queue:
        node = queue.popleft()

        if node == target:
            return visited[node]

        for next_node in (node - 1, node + 1, node * 2):
            if 0 <= next_node <= max_limit and visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
                
    return -1  # 찾을 수 없는 경우

N, K = map(int, input().rstrip().split())

# 문제에서 주어진 범위
max_limit = 100000
visited = [-1] * (max_limit + 1)
cnt = bfs(N, K)

print(cnt)
