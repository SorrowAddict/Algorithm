import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(range(1, N+1)))
lst = []
i = 0
while len(lst) < N:
    temp = arr.popleft()
    if (i+1)%K == 0:
        lst.append(temp)
    else:
        arr.append(temp)
    i += 1
print('<'+', '.join(map(str, lst))+'>')