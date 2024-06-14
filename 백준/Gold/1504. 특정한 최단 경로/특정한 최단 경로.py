from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = float('inf')


def dijkstra(num):
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


N, E = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

V1, V2 = map(int, input().rstrip().split())


# 시작점과 중간지점에 대한 최단거리를 각각 계산
# 경로A : S > V1 > V2 > N
# 경로B : S > V2 > V1 > N
s_dist = dijkstra(1)
v1_dist = dijkstra(V1)
v2_dist = dijkstra(V2)

case1 = s_dist[V1] + v1_dist[V2] + v2_dist[N]
case2 = s_dist[V2] + v2_dist[V1] + v1_dist[N]

result = min(case1, case2)

print(result if result < INF else -1)
