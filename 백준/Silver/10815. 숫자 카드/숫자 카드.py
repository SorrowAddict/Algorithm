import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

d = dict()
for x in arr:
    if x not in d:d[x] = 1
for x in check:
    print(1 if x in d else 0, end=' ')