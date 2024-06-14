from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(num, graph):
    dist = [INF] * len(graph)
    dist[num] = 0
    q = [(0, num)]

    while q:
        cost, idx = heappop(q)
        if dist[idx] < cost:
            continue

        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))

    return dist


def hacking(n, d, c):
    cnt, hacking_time = 0, 0
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        start, end, time = map(int, input().rstrip().split())
        graph[end].append((start, time))

    dist = dijkstra(c, graph)

    for i in dist:
        if i < INF:
            cnt += 1
            hacking_time = max(hacking_time, i)

    return cnt, hacking_time


INF = float('inf')
T = int(input().rstrip())

for _ in range(T):
    n, d, c = map(int, input().rstrip().split())
    print(*hacking(n, d, c))
