def bfs(i):
    visited[i] = True
    for j in adj_l[i]:
        if visited[j] == 0:
            bfs(j)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj_l = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            bfs(i)

    print(f'#{tc}', cnt)