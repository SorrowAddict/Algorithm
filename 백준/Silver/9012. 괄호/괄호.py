import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = input()
    stack = []
    for x in n:
        if x == '(':
            stack.append(x)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')