import sys
input = sys.stdin.readline

N = int(input())
Pn = 'IO'*N + 'I'
M = int(input())
S = input().strip()

cnt = 0
for i in range(M-(2*N+1)+1):
    if S[i:i+2*N+1] == Pn:
        cnt += 1
print(cnt)