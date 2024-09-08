import sys
input = sys.stdin.readline

path = []
def perm_recur(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start+1, N+1):
        path.append(i)
        perm_recur(level+1, i)
        path.pop()

N, M = map(int, input().split())
arr = list(range(1, N+1))
perm_recur(0, 0)