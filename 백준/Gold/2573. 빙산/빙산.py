import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    visited[i][j] += 1
                if visited[ni][nj] == 0 and arr[ni][nj] != 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] > 0:
                q = deque([(i, j)])
                visited[i][j] = 1
                bfs()
                cnt += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                arr[i][j] -= (visited[i][j] - 1)
                if arr[i][j] < 0: arr[i][j] = 0

    if cnt >= 2:
        print(year)
        break
    if cnt == 0:
        print(0)
        break

    year += 1