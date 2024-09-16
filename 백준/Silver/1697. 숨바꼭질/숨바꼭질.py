import sys
input = sys.stdin.readline
from collections import deque

def bfs(N, K):
    visited = [0] * 100001
    q = deque([N])
    visited[N] = 1

    while q:
        v = q.popleft()
        if v == K:
            return visited[v] - 1

        for w in (v-1, v+1, v*2):
            if 0<=w<100001 and not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1

N, K = map(int, input().split())
print(bfs(N, K))