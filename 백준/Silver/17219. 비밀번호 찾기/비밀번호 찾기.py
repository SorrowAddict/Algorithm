import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = dict()
for _ in range(N):
    email, pwd = input().strip('\n').split(' ')
    d[email] = pwd
for _ in range(M):
    print(d[input().strip('\n')])