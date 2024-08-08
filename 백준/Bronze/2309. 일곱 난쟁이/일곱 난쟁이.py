import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
arr.sort()

check_num = sum(arr)-100
for idx_x, x in enumerate(arr):
    for idx_y, y in enumerate(arr):
        if x + y == check_num and x != y and sum(arr)>100:
            arr.pop(idx_y)
            arr.pop(idx_x)
            break
print('\n'.join(str(x) for x in arr))