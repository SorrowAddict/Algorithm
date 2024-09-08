def perm_recur(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        path.append(i)
        perm_recur(level+1, i)
        path.pop()

N, M = map(int, input().split())
path = []
perm_recur(0, 1)