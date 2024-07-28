import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])
for i in sorted(lst, key= lambda x: (x[1], x[0])):
    print(i[0], i[1])