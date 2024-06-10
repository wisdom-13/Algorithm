import sys
from sys import setrecursionlimit
from collections import deque
input = sys.stdin.readline

setrecursionlimit(10 ** 6)


def dfs(idx):
    global cnt
    if visited[idx] > -1:
        return

    visited[idx] = 0
    for i in graph[idx]:
        if visited[i] == -1:  # 미방문
            visited[i] == visited[idx] + 1
            dfs(i)

    cnt += 1


N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[v].append(u)

X = int(input().rstrip())

visited = [-1] * (N + 1)
cnt = 0

dfs(X)
print(cnt - 1)
