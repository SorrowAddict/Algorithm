import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_v = 0
        cnt = 1
        for i in range(N):
            if sum_v + arr[i] > mid:
                cnt += 1
                sum_v = 0
            sum_v += arr[i]
        if sum_v == 0:
            cnt -= 1
        if cnt > M:
            start = mid + 1
        else:
            end = mid - 1
    return start

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
print(binary_search(start, end))