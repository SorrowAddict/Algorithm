import sys
input = sys.stdin.readline

def binary_search(x):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

N = int(input())
A = list(map(int, input().split()))
lst = []

for x in A:
    if not lst or lst[-1] < x:
        lst.append(x)
    else:
        idx = binary_search(x)
        lst[idx] = x
print(len(lst))