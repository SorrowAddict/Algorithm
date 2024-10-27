import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    global cnt
    cnt += 1
    visited[i] = cnt
    for j in adjL[i]:
        if not visited[j]:
            dfs(j)

N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    adjL[v].append(u)
    adjL[u].append(v)
for lst in adjL:
    lst.sort(reverse=True)
dfs(R)
for i in range(1, N+1):
    print(visited[i])