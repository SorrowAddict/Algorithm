def postorder_traversal(node):
    global lst
    if adj_l[node]:
        if len(adj_l[node]) == 3:
            postorder_traversal(adj_l[node][1])
            postorder_traversal(adj_l[node][2])
            lst.append(adj_l[node][0])
        else:
            lst.append(adj_l[node][0])
    return lst

# Testcase 만큼 반복
for tc in range(1, 11):
    N = int(input())
    adj_l = [[0]]
    for i in range(1, N+1):
        idx, *adj = map(lambda x: int(x) if x.isnumeric() else x, input().split())
        adj_l.append(adj)
    lst = []
    stack = []
    for x in postorder_traversal(1):
        if type(x) == int:
            stack.append(x)
        elif x == '+':
            stack.append(stack.pop() + stack.pop())
        elif x == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif x == '*':
            stack.append(stack.pop() * stack.pop())
        elif x == '/':
            stack.append(stack.pop(-2) // stack.pop(-1))

    print(f'#{tc}', stack[-1])