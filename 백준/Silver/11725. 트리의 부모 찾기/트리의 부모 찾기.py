import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        i = q.popleft()
        for j in graph[i]:
            if not visited[j]:
                visited[j] = i
                q.append(j)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

visited = [False] * (n+1)
q = deque([1])
visited[1] = True
bfs()

print('\n'.join(map(str, visited[2:])))