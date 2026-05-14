from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    
    for i in range(len(progresses)):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    while q:
        day = q.popleft()
        cnt = 1
        while q and day >= q[0]:
            q.popleft()
            cnt += 1
        answer.append(cnt)
    return answer