import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for x1 in arr:
    temp = 1
    for x2 in arr:
        if x1[0] < x2[0] and x1[1] < x2[1]:
            temp += 1
    print(temp, end=' ')