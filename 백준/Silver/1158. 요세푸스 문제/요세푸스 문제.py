import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(range(1, N+1)))
print('<', end='')
i, cnt = 0, 0
while cnt < N:
    temp = arr.popleft()
    if (i+1)%K == 0:
        cnt += 1
        print(temp, end='')
        if cnt != N:
            print(', ', end='')
    else:
        arr.append(temp)
    i += 1
print('>')