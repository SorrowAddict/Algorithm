import sys

n, m = map(int, sys.stdin.readline().split())
arr = [input() for _ in range(n)]

min_v = 1e7
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if arr[x][y] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[x][y] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        min_v = min(min_v, cnt1, cnt2)
print(min_v)