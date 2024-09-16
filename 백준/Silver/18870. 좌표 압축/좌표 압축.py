import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
__nums = sorted(list(set(nums)))
d = dict()
idx = 0
for i in __nums:
    if i not in d:
        d[i] = idx
        idx += 1

for i in nums:
    print(d[i], end=' ')