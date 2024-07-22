N = 1
while N != '0':
    N = input()
    if N == '0':
        pass
    else:
        for i in range(len(N)//2):
            if N[i] != N[-i-1]:
                print('no')
                break
        else:
            print('yes')