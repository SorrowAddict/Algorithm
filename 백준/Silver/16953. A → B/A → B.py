import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(A, 1)])
    while q:
        v, cnt = q.popleft()
        if v == B:
            return cnt
        lst = [v*2, int(str(v)+'1')]
        for i in lst:
            if i <= B:
                q.append((i, cnt+1))
    return -1

A, B = map(int, input().split())
print(bfs())