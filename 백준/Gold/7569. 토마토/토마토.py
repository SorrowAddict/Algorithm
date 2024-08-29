import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst):
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nz, nx, ny = z+dz[k], x+dx[k], y+dy[k]
            if 0<=nz<H and 0<=nx<N and 0<=ny<M and lst[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                lst[nz][nx][ny] = lst[z][x][y] + 1
    return lst

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

arr = bfs(arr)

result = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 0:
                print(-1)
                exit(0)
        result = max(result, max(arr[z][x]))
print(result -1)