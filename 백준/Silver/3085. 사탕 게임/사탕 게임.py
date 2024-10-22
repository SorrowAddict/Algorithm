import sys
input = sys.stdin.readline

def change():
    global max_v
    for i in range(N):
        for j in range(N):
            if i+1 < N and arr[i][j] != arr[i+1][j]:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                check_max_v()
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            if j+1 < N and arr[i][j] != arr[i][j+1]:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                check_max_v()
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return max_v

max_v = 0
def check_max_v():
    global max_v
    for i in range(N):
        tmp = 0
        prev = arr[i][0]
        for j in range(N):
            if arr[i][j] == prev:
                tmp += 1
                max_v = max(max_v, tmp)
            else: tmp = 1
            prev = arr[i][j]
    for j in range(N):
        tmp = 0
        prev = arr[0][j]
        for i in range(N):
            if arr[i][j] == prev:
                tmp += 1
                max_v = max(max_v, tmp)
            else: tmp = 1
            prev = arr[i][j]
    return max_v

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
print(change())