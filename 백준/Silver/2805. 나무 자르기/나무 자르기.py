import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        height = 0
        for x in arr:
            height += x-mid if x-mid >= 0 else 0

        if height < M:
            end = mid - 1
        elif height >= M:
            start = mid + 1
    return end

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

start, end = 1, arr[-1]
print(binary_search(start, end))