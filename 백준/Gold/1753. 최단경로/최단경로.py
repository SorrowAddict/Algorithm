import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    hq = []
    heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, now = heappop(hq)
        if distance[now] < dist:
            continue
        for cost, next in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heappush(hq, (new_cost, next))

V, E = map(int, input().split())
K = int(input())    # 시작 정점 번호
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])