import sys

input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    pcs = list(map(str, input().split()))

    if len(pcs) == 1:
        if pcs[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else: print(stack.pop())
        elif pcs[0] == 'size':
            print(len(stack))
        elif pcs[0] == 'empty':
            print(1 if len(stack) == 0 else 0)
        elif pcs[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else: print(stack[-1])
    else:
        stack.append(pcs[1])