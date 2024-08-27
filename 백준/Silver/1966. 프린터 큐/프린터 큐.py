import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    i = 1
    while arr:
        if arr[0] < max(arr):
            arr.append(arr.popleft())
        else:
            if M == 0:
                print(i)
                break
            else:
                arr.popleft()
                i += 1
        if M > 0:
            M -= 1
        else:
            M = len(arr) -1