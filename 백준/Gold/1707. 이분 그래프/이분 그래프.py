import sys
from collections import deque
input = sys.stdin.readline

def bfs(ti):
    q = deque([ti])
    visited[ti] = 1
    while q:
        i = q.popleft()
        for j in adjL[i]:
            if visited[i] == visited[j]:
                return False
            if visited[j] == -1:
                visited[j] = visited[i] ^ 1
                q.append(j)
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    visited = [-1] * (V+1)
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adjL[u].append(v)
        adjL[v].append(u)
    for i in range(1, V+1):
        if visited[i] == -1:
            if not bfs(i):
                print('NO')
                break
    else: print('YES')