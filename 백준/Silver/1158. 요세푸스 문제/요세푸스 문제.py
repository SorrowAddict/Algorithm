import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(range(1, N+1))
result = []
i = 0
while arr:
    i = (i + K - 1) % len(arr)
    result.append(arr.pop(i))
print('<' + ', '.join(map(str, result)) + '>')