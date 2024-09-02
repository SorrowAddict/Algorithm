import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    visited = [0] * (N+1)
    visited[1] = 1
    cnt = 0
    while q:
        i = q.popleft()
        for j in adj[i]:
            if not visited[j]:
                q.append(j)
                visited[j] = 1
                cnt += 1
    return cnt

N = int(input())
E = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

print(bfs())