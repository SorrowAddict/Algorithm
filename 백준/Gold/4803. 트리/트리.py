import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    is_tree = True
    while q:
        node, parent = q.popleft()
        for next in adjL[node]:
            if not visited[next]:
                visited[next] = True
                q.append((next, node))
            elif next != parent:
                is_tree = False
    return is_tree

tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    adjL = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)
    visited = [False] * (n + 1)
    q = deque()
    tree = 0
    for i in range(1, n + 1):
        if not visited[i]:
            q.append((i, 0))
            visited[i] = True
            if bfs():
                tree += 1
    if tree == 0:
        print(f'Case {tc}: No trees.')
    elif tree == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {tree} trees.')