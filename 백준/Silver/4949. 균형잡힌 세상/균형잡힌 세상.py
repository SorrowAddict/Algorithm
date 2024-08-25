# 4949. 균형잡힌 세상 [문자열, 스택]

while 1:
    words = input()
    if words == '.':
        break
    stack = []
    for x in words:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if not stack:
                print('no')
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif x == ']':
            if not stack:
                print('no')
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')