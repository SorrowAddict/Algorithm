import sys
input = sys.stdin.readline

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

if n in S:
    print(0)
else:
    min, max = 0, 0
    for x in S:
        if x < n:
            min = x
        elif x > n and max == 0:
            max = x
    max -= 1
    min += 1
    print((n - min) * (max - n + 1) + (max - n))