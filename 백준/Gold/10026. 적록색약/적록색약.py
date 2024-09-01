# 10026. 적록색약

import sys
from collections import deque
input = sys.stdin.readline

def bfs(ti, tj):
    q.append((ti, tj))
    visited[ti][tj] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
q = deque()

# RGB
rgb = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            rgb += 1

# not RGB
visited = [[0]*N for _ in range(N)]
not_rgb = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            not_rgb += 1
print(rgb, not_rgb)