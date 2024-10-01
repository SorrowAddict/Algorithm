import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
def dijkstra(start):
    hq = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if distance[now] < dist:
            continue
        for next, cost in arr[now]:
            new_cost = cost + dist
            if distance[next] > new_cost:
                distance[next] = new_cost
                hq.append((new_cost, next))
    return distance[arrival]

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(int(input())):
    v1, v2, w = map(int, input().split())
    arr[v1].append((v2, w))
departure, arrival = map(int, input().split())
print(dijkstra(departure))