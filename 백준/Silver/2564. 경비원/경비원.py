# 2564. 경비원

import sys
input = sys.stdin.readline

def f(dr, l):
    if dr == 1:
        return l
    if dr == 2:
        return h + w + h - l
    if dr == 3:
        return h + w + h + w - l
    if dr == 4:
        return h + l

h, w = map(int, input().split())

lst = []
for _ in range(int(input())+1):
    dr, l = map(int, input().split())
    lst.append([dr, l])

result = 0
dr, l = lst[-1]
check = f(dr, l)
for dr, l in lst[:-1]:
    temp = min(abs(check - f(dr, l)), 2*w+2*h-abs(check - f(dr, l)))
    result+=temp

print(result)