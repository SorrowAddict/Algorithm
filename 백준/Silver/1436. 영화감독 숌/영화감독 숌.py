import sys
input = sys.stdin.readline

N = int(input())

lst = []
num = 0
while 1:
    num += 1
    if '666' in str(num):
        lst.append(num)
        if len(lst) == N:
            print(lst[-1])
            break