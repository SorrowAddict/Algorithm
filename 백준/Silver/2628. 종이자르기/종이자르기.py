import sys

input = sys.stdin.readline

row, col = map(int, input().split())

n = int(input())

row_list, col_list = [], []
row_list.append(0)
row_list.append(row)
col_list.append(0)
col_list.append(col)

for _ in range(n):
    rc, l = map(int, input().split())
    if rc == 0:
        col_list.append(l)
    else:
        row_list.append(l)
row_list = sorted(row_list)
col_list = sorted(col_list)

for i in range(len(row_list)-1, 0, -1):
    row_list[i] -= row_list[i-1]

for i in range(len(col_list)-1, 0, -1):
    col_list[i] -= col_list[i-1]

check_list = []
for x in row_list:
    for y in col_list:
        check_list.append(x * y)

print(max(check_list))