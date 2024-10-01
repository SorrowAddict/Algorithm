import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (V+1)
    distance[start] = 0
    hq = []
    heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if distance[now] < dist:
            continue
        for next, cost in arr[now]:
            new_cost = cost + dist
            if distance[next] > new_cost:
                distance[next] = new_cost
                heappush(hq, (new_cost, next))
    return distance

V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
v1, v2 = map(int, input().split())

one_to_fin = dijkstra(1)
v1_to_fin = dijkstra(v1)
v2_to_fin = dijkstra(v2)

path1 = one_to_fin[v1] + v1_to_fin[v2] + v2_to_fin[V]
path2 = one_to_fin[v2] + v2_to_fin[v1] + v1_to_fin[V]
ans = min(path1, path2)
print(ans if ans < INF else -1)