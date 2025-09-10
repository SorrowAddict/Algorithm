import sys
input = sys.stdin.readline

N = int(input())
tmp = N
cnt = 0

while True:
    a = tmp // 10
    b = tmp % 10
    c = (a + b) % 10
    tmp = (b * 10) + c
    cnt += 1
    if tmp == N:
        break
print(cnt)