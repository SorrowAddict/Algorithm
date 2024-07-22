N = input()
while N != '0':
    for i in range(len(N)//2):
        if N[i] != N[-i-1]:
            print('no')
            break
    else:
        print('yes')
    N = input()