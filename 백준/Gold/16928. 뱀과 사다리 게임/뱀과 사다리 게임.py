import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        i = q.popleft()
        for j in range(1, 7):
            ni = i + j
            if ni > 100:
                continue
            if ni in ladder:
                ni = ladder[ni]
            if ni in snake:
                ni = snake[ni]
            if not arr[ni]:
                arr[ni] = arr[i] + 1
                q.append(ni)

            if ni == 100:
                return arr[i]

N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

arr = [0] * 101
q = deque([1])
arr[1] = 1
print(bfs())