import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        i, j = q.popleft()
        for di, dj  in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and arr[ni][nj] > h:
                    visited[ni][nj] = 1
                    q.append((ni, nj))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_h = max(map(max, arr))
ans = 0
for h in range(max_h + 1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] > h:
                visited[i][j] = 1
                q = deque([(i, j)])
                bfs()
                cnt += 1
    ans = max(ans, cnt)
print(ans)