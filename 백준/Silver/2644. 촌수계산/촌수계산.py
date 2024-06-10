import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    global N
    visited = [-1] * (N + 1)
    queue = deque([start])
    visited[start] = 0
    while queue:
        node = queue.popleft()
        for adj in sorted(graph[node]):
            if visited[adj] == -1:
                visited[adj] = visited[node] + 1
                queue.append(adj)

    return visited


N = int(input().rstrip())
A, B = map(int, input().rstrip().split())
M = int(input().rstrip())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# A에서의 B까지의 거리
visited = bfs(A)
print(visited[B])
