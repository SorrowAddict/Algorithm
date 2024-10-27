import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([R])
    cnt = 1
    visited[R] = cnt
    while q:
        i = q.popleft()
        for j in adjL[i]:
            if not visited[j]:
                q.append(j)
                cnt += 1
                visited[j] = cnt

N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    adjL[v].append(u)
    adjL[u].append(v)
for lst in adjL:
    lst.sort()
bfs()
for i in range(1, N+1):
    print(visited[i])