from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(cnt):
    global max_v

    try_cnt = 1
    while try_cnt < N+2:
        if cnt * M - cost_list[try_cnt] >= 0:
            max_v = max(max_v, cnt)
        try_cnt += 1

        for _ in range(len(q)):
            ti, tj = q.popleft()
            for k in range(4):
                ni, nj = ti+di[k], tj+dj[k]
                if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                    if arr[ni][nj] == 1:
                        cnt += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost_list = [K**2 + (K-1)**2 for K in range(N+2)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            q = deque([(i, j)])
            visited[i][j] = 1
            temp = 0
            if arr[i][j] == 1:
                temp = 1
            bfs(temp)
    print(f'#{tc}', max_v)