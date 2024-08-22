# 11866. 요세푸스 문제 0

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
que = deque([i for i in range(1, N+1)])

result = []
while que:
    for _ in range(K-1):
        que.append(que.popleft())
    result.append(str(que.popleft()))
print('<'+', '.join(result)+'>')