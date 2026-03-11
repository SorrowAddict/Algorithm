import sys
input = sys.stdin.readline

def dfs(idx, depth):
    global ans

    if depth == M:
        tmp = 0
        for i in house:
            dist = 1e9
            for j in chicken:
                if visited[chicken.index(j)]:
                    dist = min(dist, abs(i[0] - j[0]) + abs(i[1] - j[1]))
            tmp += dist
        ans = min(ans, tmp)
        return

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, depth + 1)
            visited[i] = False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house, chicken = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

ans = 1e9
visited = [False] * len(chicken)
dfs(0, 0)
print(ans)