dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs_recur(y, x, temp, total, is_check):
    global ans
    for k in range(4):
        ny, nx = y+dy[k], x+dx[k]
        if 0<=ny<N and 0<=nx<N and arr[ny][nx] < temp and not visited[ny][nx]:
            visited[y][x] = 1
            dfs_recur(ny, nx, arr[ny][nx], total + 1, is_check)
            visited[y][x] = 0
        elif is_check and 0<=ny<N and 0<=nx<N and arr[ny][nx]-K < temp and not visited[ny][nx]:
            original_height = arr[ny][nx]
            arr[ny][nx] = temp - 1
            visited[y][x] = 1
            dfs_recur(ny, nx, arr[ny][nx], total + 1, False)
            visited[y][x] = 0
            arr[ny][nx] = original_height
    ans = max(ans, total)

def find_start():
    global max_v
    max_v = 0
    for row in arr:
        max_v = max(max_v, max(row))

    _set = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_v:
                _set.add((i, j))
    return _set

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0
    for y, x in find_start():
        visited[y][x] = 1
        dfs_recur(y, x, max_v, 1, True)
        visited[y][x] = 0
    print(f'#{tc}', ans)