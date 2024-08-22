import sys
from collections import deque
input = sys.stdin.readline

def f(order):
    if order[0] == 'push':
        que.append(order[1])
    elif order[0] == 'pop':
        print(que.popleft()) if que else print(-1)
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        print(0) if que else print(1)
    elif order[0] == 'front':
        print(que[0]) if que else print(-1)
    elif order[0] == 'back':
        print(que[-1]) if que else print(-1)

que = deque()
N = int(input())
for _ in range(N):
    order = list(input().split())
    f(order)