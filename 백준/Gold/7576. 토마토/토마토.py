import sys
from collections import deque
input = sys.stdin.readline

def bfs(ij_lst, lst):
    if not ij_lst:
        return -1

    q = deque(ij_lst)

    max_v = 0
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<N and 0<=nj<M and lst[ni][nj] == 0:
                q.append([ni, nj])
                lst[ni][nj] = lst[ti][tj] + 1
                max_v = max(max_v, lst[ni][nj])

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                return -1
    return max_v -1

def find_start(arr):
    temp = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                temp.append([i, j])
            if arr[i][j] == 0:
                cnt += 1
    if cnt == 0:
        return 'No'
    else:
        return temp

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
if find_start(arr) == 'No':
    print(0)
else:
    print(bfs(find_start(arr), arr))