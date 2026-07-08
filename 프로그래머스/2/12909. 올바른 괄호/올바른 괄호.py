def solution(s):
    answer = True
    
    stack = []
    
    for x in s:
        if x == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    return True