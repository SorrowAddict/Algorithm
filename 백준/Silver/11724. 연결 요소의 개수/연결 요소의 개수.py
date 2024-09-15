import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    global cnt
    q = deque([s])
    visited[s] = True

    while q:
        v = q.popleft()
        for i in adjL[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    cnt += 1

V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

cnt = 0
for i in range(1, V+1):
    if not visited[i]:
        bfs(i)
print(cnt)