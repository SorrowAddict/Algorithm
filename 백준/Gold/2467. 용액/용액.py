import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

l, r = 0, N-1
min_v = int(1e11)
while l < r:
    x = arr[l]+arr[r]
    if abs(x) <= min_v:
        i, j = arr[l], arr[r]
        min_v = abs(x)
    if x <= 0:
        l += 1
    else:
        r -= 1
print(i, j)