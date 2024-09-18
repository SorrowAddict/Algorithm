import sys
from collections import deque
input = sys.stdin.readline

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
def bfs(i, j):
    cnt = 1
    q = deque([(i, j)])
    arr[i][j] = 0
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]:
                cnt += 1
                q.append((ni, nj))
                arr[ni][nj] = 0
    lst.append(cnt)

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            bfs(i, j)
print(len(lst))
for i in sorted(lst):
    print(i)