import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x: (x[0], x[1]))
e = arr[-1][1]
i, cnt = N, 0
while i > 0:
    i -= 1
    if arr[i][1] <= e:
        cnt += 1
        e = arr[i][0]
print(cnt)