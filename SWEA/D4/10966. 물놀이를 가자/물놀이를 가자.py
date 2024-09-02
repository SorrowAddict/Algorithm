from collections import deque

def bfs():
    result = 0
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr_wl[ni][nj]==-1:
                q.append((ni, nj))
                arr_wl[ni][nj] = arr_wl[i][j]+1
                result += arr_wl[ni][nj]
    return result

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr_wl = [[-1]*M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                arr_wl[i][j] = 0
                q.append((i, j))
    print(f'#{tc}', bfs())