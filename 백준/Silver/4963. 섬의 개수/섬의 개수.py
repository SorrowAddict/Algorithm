import sys
input = sys.stdin.readline
from collections import deque

def bfs(lst):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if lst[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = 1
                q.append((i, j))
                bfs(arr)
    print(cnt)