import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start, end = 1, sorted(arr)[-1]
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for x in arr:
        temp += x//mid
    if temp >= N:
        start = mid + 1
    elif temp < N:
        end = mid - 1
print(end)