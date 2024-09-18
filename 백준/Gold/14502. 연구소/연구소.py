import sys
from collections import deque
input = sys.stdin.readline

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
def bfs(tmp_arr):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                q.append((i, j))

    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and tmp_arr[ni][nj] == 0:
                tmp_arr[ni][nj] = 2
                q.append((ni, nj))

    cnt = sum(row.count(0) for row in tmp_arr)
    return cnt

def add_walls(wall_count, start):
    global max_v
    if wall_count == 3:
        max_v = max(max_v, bfs([row[:] for row in arr]))
        return

    for i in range(start, len(empty_spaces)):
        x, y = empty_spaces[i]
        arr[x][y] = 1
        add_walls(wall_count + 1, i + 1)
        arr[x][y] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_v = 0
empty_spaces = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 0]
add_walls(0, 0)
print(max_v)