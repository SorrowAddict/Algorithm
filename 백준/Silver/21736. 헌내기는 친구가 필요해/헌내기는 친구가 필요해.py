import sys
from collections import deque

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I':
                return i, j

def bfs():
    cnt = 0
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] != 'X':
                if arr[ni][nj] == 'P':
                    cnt += 1
                q.append((ni, nj))
                visited[ni][nj] = True
    return cnt

N, M = map(int, sys.stdin.readline().split())
arr = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
i, j = find_start()
q = deque([(i, j)])
visited[i][j] = True

ans = bfs()
if ans == 0:
    print('TT')
else:
    print(ans)