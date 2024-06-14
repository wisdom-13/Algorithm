from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(num):
    dist = [INF] * len(graph)
    dist[num] = 0
    q = [(0, num)]

    while q:
        cost, idx = heappop(q)
        if dist[idx] < cost:  # 현재 최단거리보다 크면 계산하지 않음
            continue

        # 현재 위치에서 갈 수 있는 위치의 비용 계산
        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))

    return dist


INF = float('inf')
N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, price = map(int, input().rstrip().split())
    graph[start].append((end, price))

S, E = map(int, input().rstrip().split())

print(dijkstra(S)[E])