from math import factorial

N = int(input())

cnt = 0
for _ in str(factorial(N))[::-1]:
    if _ == '0':
        cnt+=1
    else:
        break
print(cnt)