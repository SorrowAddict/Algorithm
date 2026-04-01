import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(n, m):
    que = deque()
    que.append([n, m])
    vst[n][m] = True
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not vst[nx][ny] and grid[nx][ny] > 0:
                que.append([nx, ny])
                vst[nx][ny] = True

N, M = map(int, input().split())

stk = []
grid = [([0] * M) for _ in range(N)]
for i in range(N):
    grid[i] = list(map(int, input().split()))
    for j in range(M):
        if grid[i][j] > 0:
            stk.append([i, j])
    
vst = [([False] * M) for _ in range(N)]

ans = 0
while True:
    sep = 0
    for x, y in stk:
        if not vst[x][y]:
            bfs(x, y)
            sep += 1
    if sep > 1:
        print(ans)
        exit()
        
    diffs = []
    for x, y in stk:
        vst[x][y] = False
        
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if grid[nx][ny] == 0:
                cnt += 1
    
        if cnt > 0:
            diffs.append([x, y, -cnt])
    
    if len(diffs) == 0:
        print(0)
        exit()
    
    ans += 1

    for x, y, c in diffs:
        grid[x][y] += c
        if grid[x][y] < 0:
            grid[x][y] = 0
        
    tmp = []
    for x, y in stk:
        if grid[x][y] > 0:
            tmp.append([x, y])
    stk = tmp