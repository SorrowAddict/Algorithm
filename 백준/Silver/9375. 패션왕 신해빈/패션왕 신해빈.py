import sys
input = sys.stdin.readline


for _ in range(int(input())):
    d = dict()
    for _ in range(int(input())):
        item, type = map(str, input().strip().split())
        if type in d:
            d[type] += 1
        else:
            d[type] = 1

    cnt = 1
    for v in d.values():
        cnt *= v+1
    print(cnt -1)