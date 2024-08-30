import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
                if ni == N-1 and nj == M-1:
                    return arr[i][j] + 1
                q.append((ni, nj))
                arr[ni][nj] = arr[i][j] + 1

N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

q = deque([(0, 0)])

print(bfs())