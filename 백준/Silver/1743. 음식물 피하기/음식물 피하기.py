import sys
from collections import deque
input = sys.stdin.readline

def bfs(ti, tj):
    q = deque([(ti, tj)])
    arr[ti][tj] = 0
    cnt = 0
    while q:
        i, j = q.popleft()
        cnt += 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]:
                arr[ni][nj] = 0
                q.append((ni, nj))
    return cnt

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            max_v = max(max_v, bfs(i, j))
print(max_v)