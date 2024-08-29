import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_l = [int(input()) for _ in range(N)]

cnt = 0
for i in reversed(coin_l):
    if K//i > 0:
        cnt += K//i
        K = K%i
        if K == 0:
            break
print(cnt)