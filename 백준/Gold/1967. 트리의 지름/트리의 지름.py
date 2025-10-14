import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def bfs(start):
    visited = [False] * (n + 1)
    q = deque([(start, 0)])
    visited[start] = True
    max_node, max_distance = start, 0
    
    while q:
        node, dist = q.popleft()
        if dist > max_distance:
            max_distance = dist
            max_node = node
        for nxt, w in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, dist + w))
    
    return max_node, max_distance

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

first_node, _ = bfs(1)
_, ans = bfs(first_node)
print(ans)