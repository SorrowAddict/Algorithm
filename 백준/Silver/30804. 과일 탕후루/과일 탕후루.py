import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

d = dict()
max_v = 0
left = 0
for right in range(N):
    if arr[right] in d:
        d[arr[right]] += 1
    else:
        d[arr[right]] = 1
    while len(d) > 2:
        d[arr[left]] -= 1
        if d[arr[left]] == 0:
            del d[arr[left]]
        left += 1
    max_v = max(max_v, right-left+1)
print(max_v)