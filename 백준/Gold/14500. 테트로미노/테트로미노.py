import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [([0] * M) for _ in range(N)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visited[r][c] = 0

print(ans)