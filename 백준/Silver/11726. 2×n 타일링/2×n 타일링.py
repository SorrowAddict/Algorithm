import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+2)
d[1], d[2] = 1, 2
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]
if n == 1 or n == 2:
    print(n)
else:
    print(d[n]%10007)