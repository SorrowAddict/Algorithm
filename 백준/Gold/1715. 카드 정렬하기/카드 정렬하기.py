import sys
import heapq
input = sys.stdin.readline

l = []
N = int(input())

for _ in range(N):
    n = int(input())
    heapq.heappush(l, n)

result = 0
while len(l) > 1:
    temp_1 = heapq.heappop(l)
    temp_2 = heapq.heappop(l)
    result += temp_1 + temp_2
    heapq.heappush(l, temp_1 + temp_2)

print(result)