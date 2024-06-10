import sys
from sys import setrecursionlimit
from collections import deque
input = sys.stdin.readline

setrecursionlimit(10 ** 6)


def dfs(idx):
    global answer
    if visited[idx] > -1:
        return

    visited[idx] = 0

    if len(graph[idx]) == 0:  # 마지막
        answer = 'yes'

    for i in graph[idx]:
        if i in s_list:
            visited[i] = visited[idx] + 1
        dfs(i)


N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

S = int(input().rstrip())
s_list = list(map(int, input().rstrip().split()))


visited = [-1] * (N + 1)

answer = 'Yes'
cnt = 0

if 1 in s_list:
    print('Yes')
else:
    dfs(1)
    print(answer)
