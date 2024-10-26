import sys
input = sys.stdin.readline

X = int(input())
for _ in range(int(input())):
     a, b = map(int, input().split())
     X -= a * b
if X == 0: print('Yes')
else: print('No')