import sys
from collections import deque
input = sys.stdin.readline

def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
def bfs():
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and arr[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = True
                arr[ni][nj] = arr[ti][tj] + 1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
i, j = find_start()
q = deque([(i, j)])
visited[i][j] = True
arr[i][j] = 0
bfs()

for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            arr[i][j] = -1

for row in arr:
    print(*row)