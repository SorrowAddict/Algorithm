import sys
input = sys.stdin.readline

N = int(input())

max_v = 0
result = []
for i in range(1, N+1):
    lst = [N, i]
    while 1:
        if lst[-2] - lst[-1] < 0:
            break
        lst.append(lst[-2] - lst[-1])
    if max_v < len(lst):
        max_v = len(lst)
        result = lst
print(max_v)
print(*result)