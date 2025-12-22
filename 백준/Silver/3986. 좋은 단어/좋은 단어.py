N = int(input())
cnt = 0
for _ in range(N):
    stack = []
    lst = list(input())
    for x in lst:
        if not stack:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    if not stack:
        cnt += 1
print(cnt)