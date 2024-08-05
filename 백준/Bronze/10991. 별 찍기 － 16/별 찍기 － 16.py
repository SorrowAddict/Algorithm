N = int(input())

for i in range(1, N+1):
    if i == 1:
        print(' '*abs(i-N)+'*')
    else:
        lst = []
        for _ in range(1, i+1):
            lst.append('*')
        print(' '*(N-i), end='')
        print(*lst)