import sys
import heapq
input = sys.stdin.readline

min_v = []

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(min_v):
            print(heapq.heappop(min_v))
        else:
            print(0)
    else:
        heapq.heappush(min_v, n)