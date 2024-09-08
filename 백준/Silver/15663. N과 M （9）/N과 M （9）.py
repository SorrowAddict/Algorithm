def perm_recur(n):
    if n == M:
        print(*path)
        return

    check = 0
    for i in range(len(arr)):
        if not used[i] and check != arr[i]:
            path.append(arr[i])
            used[i] = True
            check = arr[i]
            perm_recur(n+1)
            used[i] = False
            path.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * N
path = []
perm_recur(0)