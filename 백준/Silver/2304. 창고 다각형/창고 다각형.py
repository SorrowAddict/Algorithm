import sys
input = sys.stdin.readline

lst = []
N = int(input())
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()

max_v = max(lst, key=lambda x: x[1])
result = max_v[1]
idx = lst.index(max_v)

height = lst[0][1]
for i in range(idx):
    if height < lst[i+1][1]:
        result += height * (lst[i+1][0]-lst[i][0])
        height = lst[i+1][1]
    else:
        result += height * (lst[i+1][0] - lst[i][0])

height = lst[-1][1]
for i in range(N-1, idx, -1):
    if height < lst[i-1][1]:
        result += height * (lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else:
        result += height * (lst[i][0] - lst[i-1][0])

print(result)