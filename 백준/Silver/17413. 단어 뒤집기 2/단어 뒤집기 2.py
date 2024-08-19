import sys
from collections import deque
# input = sys.stdin.readline

S = input()
que = deque()
chk = False

result = ''
for x in S:
    if x == '<':
        chk = True
        for  _ in range(len(que)):
            result += que.pop()
    que.append(x)
    if x == '>':
        chk = False
        while que:
            result += que.popleft()
    if x == ' ' and chk == False:
        for _ in range(len(que)):
            if _ == 0:
                que.pop()
            else:
                result += que.pop()
        result += ' '
else:
    while que:
        result += que.pop()
print(result)