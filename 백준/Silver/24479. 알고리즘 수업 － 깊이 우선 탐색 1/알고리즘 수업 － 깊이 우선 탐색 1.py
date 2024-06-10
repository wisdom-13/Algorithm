import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, order):
    visited[node] = order
    order += 1
    for adj in sorted(graph[node]):
        if visited[adj] == 0:
            order = dfs(adj, order)
    return order

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
dfs(R, 1)

for i in range(1, N + 1):
    print(visited[i])
