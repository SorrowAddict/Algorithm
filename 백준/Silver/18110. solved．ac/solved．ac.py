import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    l = [int(input()) for _ in range(n)]
    temp = my_round(n*0.15)
    if n == 1:
        print(*l)
    else:
        print(my_round((sum(sorted(l)[temp:-temp])/(n-2*temp))))