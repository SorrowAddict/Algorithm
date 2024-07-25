x, y = map(int, input().split())
while 1:
    if x==0 and y==0:
        break
    else:
        if x>y:
            print('Yes')
        else:
            print('No')
        x, y = map(int, input().split())