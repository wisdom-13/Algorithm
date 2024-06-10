import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    order = 1
    visited[start] = order
    while queue:
        node = queue.popleft()
        for adj in sorted(graph[node]):
            if visited[adj] == 0:
                order += 1
                visited[adj] = order
                queue.append(adj)

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
bfs(R)

for i in range(1, N + 1):
    print(visited[i])