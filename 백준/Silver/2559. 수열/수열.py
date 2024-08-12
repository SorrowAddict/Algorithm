import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

stack = deque(arr[:K])
stack_sum = sum(stack)
max_v = stack_sum

for i in range(K, N):
    stack_sum += arr[i] - stack.popleft()
    stack.append(arr[i])
    if max_v < stack_sum:
        max_v = stack_sum

print(max_v)