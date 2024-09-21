import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (N+1)
    q = deque([start])
    visited[start] = 0

    while q:
        i = q.popleft()
        for j in adjL[i]:
            if visited[j] == -1:
                visited[j] = visited[i] + 1
                q.append(j)
    return sum(visited)

N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

i, min_v = 0, 1e9
for i in range(1, N+1):
    total = bfs(i)
    if min_v > total:
        min_v = total
        ans = i
print(ans)