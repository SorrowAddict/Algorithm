import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    n = int(input())
    lst.append(n)
for i in sorted(lst):
    print(i)