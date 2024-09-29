import sys
input = sys.stdin.readline

def back_tracking(level):
    if len(path) == M:
        print(*path)
        return

    for i in range(level, len(arr)):
        path.append(arr[i])
        back_tracking(i)
        path.pop()

N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
path = []
back_tracking(0)