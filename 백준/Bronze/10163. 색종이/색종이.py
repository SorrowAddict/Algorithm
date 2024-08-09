import sys
input=sys.stdin.readline

arr = [[0] * 1001 for _ in range(1001)]
N = int(input())
cnt_N = [0]*(N+1)
for i in range(1, N+1):
    row, col, row_l, col_l = map(int, input().split())
    for x in range(row, row+row_l):
        for y in range(col, col+col_l):
            if arr[x][y] != 0:
                cnt_N[arr[x][y]] -= 1
            arr[x][y] = i
            cnt_N[i] += 1
print('\n'.join(map(str, cnt_N[1:])))