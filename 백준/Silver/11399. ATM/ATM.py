import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

d = [0] * (N+1)
for i in range(N):
    d[i] = d[i-1]+arr[i]
print(sum(d))