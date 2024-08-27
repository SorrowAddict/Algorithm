import sys
input = sys.stdin.readline

n = int(input())
stack, result = [], []
cnt = 1
for i in range(n):
    m = int(input())
    while cnt <= m:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == m:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(result))