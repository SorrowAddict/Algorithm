import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
_arr = sorted(list(set(arr)))
d = dict()
for i in range(len(_arr)):
    d[_arr[i]] = i
print(' '.join(str(d[x]) for x in arr))