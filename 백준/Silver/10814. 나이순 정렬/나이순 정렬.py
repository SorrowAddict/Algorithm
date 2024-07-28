import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    lst.append([int(age), name])
for i in sorted(lst, key=lambda x:(x[0])):
    print(i[0], i[1])