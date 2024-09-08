import sys
input = sys.stdin.readline

def perm_recur(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if not used[i]:
            path.append(arr[i])
            used[i] = True
            perm_recur(level + 1)
            used[i] = False
            path.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * N
path = []
perm_recur(0)