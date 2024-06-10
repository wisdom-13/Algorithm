import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, k):
    queue = deque([start])
    visited[start] = 0
    k_list = []
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if visited[adj] == -1:
                visited[adj] = visited[node] + 1
                queue.append(adj)
                if visited[adj] == k:
                    k_list.append(adj)

    return k_list


N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

visited = [-1] * (N + 1)
k_list = bfs(X, K)

if len(k_list) > 0:
    print(*sorted(k_list), sep='\n')
else:
    print(-1)
