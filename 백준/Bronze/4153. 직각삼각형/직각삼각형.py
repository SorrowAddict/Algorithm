lst = sorted(list(map(int, input().split())))
while 1:
    if 0 in lst:
        break
    elif lst[0]**2+lst[1]**2==lst[2]**2:
        print('right')
    else:
        print('wrong')
    lst = sorted(map(int, input().split()))