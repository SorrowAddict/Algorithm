import sys
input = sys.stdin.readline
from bisect import bisect_left

N, H = map(int, input().split())
up, down = [], []

for i in range(N):
    x = int(input())
    if i % 2:
        up.append(x)
    else:
        down.append(x)

up.sort()
down.sort()

min_num = 1e9
min_cnt = 1

for i in range(1, H + 1):
    up_idx, down_idx = bisect_left(up, (H + 1) - i), bisect_left(down, i)
    cnt = N - (up_idx + down_idx)

    if cnt < min_num:
        min_num = cnt
        min_cnt = 1
    elif cnt == min_num:
        min_cnt += 1
print(min_num, min_cnt)