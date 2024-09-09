from collections import deque

# 우하좌상 -> 5, 7, 11, 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
check = [(1, 3, 6, 7), (1, 2, 4, 7), (1, 3, 4, 5), (1, 2, 5, 6)]

def bfs():
    try_cnt, cnt = 1, 1
    while try_cnt < L:
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in path_direction(arr[i][j]):
                ni, nj = i+di[k], j+dj[k]
                if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] != 0:
                    if arr[ni][nj] in check[k]:
                        q.append((ni, nj))
                        visited[ni][nj] = True
                        cnt += 1
        try_cnt += 1
    return cnt

def path_direction(n):
    if n == 1:
        return (0, 1, 2, 3)
    if n == 2:
        return (1, 3)
    if n == 3:
        return (0, 2)
    if n == 4:
        return (0, 3)
    if n == 5:
        return (0, 1)
    if n == 6:
        return (1, 2)
    if n == 7:
        return (2, 3)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # M*N 배열, 맨홀 위치 (R, C), 시간 L
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    q = deque([(R, C)])
    visited[R][C] = True
    print(f'#{tc}', bfs())