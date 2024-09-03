import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    d = [0] * (N+6)
    d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
    if 1<=N<=5:
        print(d[N])
    else:
        for i in range(6, N+1):
            d[i] = d[i-1] + d[i-5]
        print(d[N])