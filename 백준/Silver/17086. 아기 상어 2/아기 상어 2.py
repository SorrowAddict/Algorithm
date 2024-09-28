import sys
from collections import deque
input = sys.stdin.readline

di = (0, 1, 0, -1, -1, -1, 1, 1)
dj = (1, 0, -1, 0, -1, 1, -1, 1)
def bfs():
    global max_v

    while q:
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))
                max_v = max(max_v, arr[ni][nj])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            q.append((i, j))
bfs()
print(max_v-1)