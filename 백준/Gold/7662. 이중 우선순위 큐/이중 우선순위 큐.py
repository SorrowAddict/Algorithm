import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for _ in range(int(input())):
    min_hq = list()
    max_hq = list()
    check = dict()
    for _ in range(int(input())):
        s, n = input().split()
        n = int(n)
        if s == 'I':
            heappush(min_hq, n)
            heappush(max_hq, -n)
            if n not in check:
                check[n] = 0
            check[n] += 1

        elif s == 'D':
            if n == -1:
                while min_hq and check[min_hq[0]] == 0:
                    heappop(min_hq)
                if min_hq:
                    min_val = heappop(min_hq)
                    check[min_val] -= 1

            elif n == 1:
                while max_hq and check[-max_hq[0]] == 0:
                    heappop(max_hq)
                if max_hq:
                    max_val = heappop(max_hq)
                    check[-max_val] -= 1

    while min_hq and check[min_hq[0]] == 0:
        heappop(min_hq)

    while max_hq and check[-max_hq[0]] == 0:
        heappop(max_hq)

    if not min_hq or not max_hq:
        print("EMPTY")
    else:
        min_val = min_hq[0]
        max_val = -max_hq[0]
        print(max_val, min_val)