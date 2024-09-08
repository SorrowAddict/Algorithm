import sys
input = sys.stdin.readline

def comb_recur(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start+1, N+1):
        path.append(i)
        comb_recur(level+1, i)
        path.pop()

N, M = map(int, input().split())
path = []
comb_recur(0, 0)