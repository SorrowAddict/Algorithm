import sys
input = sys.stdin.readline

def multi(A, B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += A[i][k] * B[k][j]
            tmp[i][j] %= 1000
    return tmp

def square(b):
    if b == 1:
        return arr
    half = square(b // 2)
    if b % 2 == 0:
        return multi(half, half)
    else:
        return multi(multi(half, half), arr)

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = square(B)
for i in range(N):
    for j in range(N):
        print(ans[i][j] % 1000, end=' ')
    print()