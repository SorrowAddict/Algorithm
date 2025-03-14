import sys
from collections import deque
input = sys.stdin.readline

di = (1, 2, 2, 1, -1, -2, -2, -1)
dj = (2, 1, -1, -2, -2, -1, 1, 2)
def bfs():
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<l and 0<=nj<l and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))
                if ni == x2 and nj == y2:
                    return arr[ni][nj] -1
    return 0

for _ in range(int(input())):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    arr = [[False] * l for _ in range(l)]
    q = deque([(x1, y1)])
    arr[x1][y1] = True
    print(bfs())