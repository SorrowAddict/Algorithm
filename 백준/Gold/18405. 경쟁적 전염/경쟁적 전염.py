import sys
from collections import deque
input = sys.stdin.readline

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
def bfs():
    while q:
        virus, time, ti, tj = q.popleft()
        if time == S:
            break
        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = virus
                q.append((virus, time + 1, ni, nj))

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            lst.append((arr[i][j], 0, i, j))

q = deque(sorted(lst))
bfs()
print(arr[X-1][Y-1])