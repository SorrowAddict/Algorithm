N = int(input())

for i in range(1, N+1):
    if i == 1:
        print(' '*abs(i-N)+'*')
    else:
        print(' '*abs(i-N)+'*'+' '*((i-2)*2+1)+'*')