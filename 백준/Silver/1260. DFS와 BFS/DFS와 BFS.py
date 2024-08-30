# 1260. DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

stack = []
def dfs(s, lst):
    global stack
    lst[s] = 1
    stack.append(s)
    for x in node[s]:
        if not lst[x]:
            dfs(x, lst)
    return stack

def bfs():
    temp = []
    visited = [0] * (N + 1)
    while q:
        i = q.popleft()
        if not visited[i]:
            visited[i] = 1
            temp.append(i)
            for x in node[i]:
                if not visited[x]:
                    q.append(x)
    return temp

# N 정점의 개수, M 간선의 개수, V 탐색 시작할 정점의 번호
N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    node[v1].append(v2)
    node[v2].append(v1)

for i in range(len(node)):
    node[i].sort()
# node = [sorted(n) for n in node]

q = deque([V])

visited = [0] * (N + 1)
print(*dfs(V, visited))
print(*bfs())