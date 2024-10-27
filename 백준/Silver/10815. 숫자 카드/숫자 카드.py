import sys
input = sys.stdin.readline

def binary_search(x):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
for x in check:
    print(1 if binary_search(x) else 0, end=' ')