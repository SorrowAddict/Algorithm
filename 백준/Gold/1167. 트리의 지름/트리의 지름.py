import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (V + 1)
    visited[start] = 0
    res = [0, 0]
    while q:
        node, dist = q.popleft()
        for nxt, w in adjL[node]:
            if visited[nxt] == -1:
                q.append((nxt, dist + w))
                visited[nxt] = dist + w
                if res[1] < dist + w:
                    res[0], res[1] = nxt, dist + w
    return res

V = int(input())
adjL = [[] for _ in range(V + 1)]
for _ in range(V):
    tmp = list(map(int, input().split()))
    cnt_node = tmp[0]
    idx = 1
    while tmp[idx] != -1:
        adjL[cnt_node].append((tmp[idx], tmp[idx + 1]))
        idx += 2

node, _ = bfs(1)
print(bfs(node)[1])