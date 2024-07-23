T = int(input())
for i in range(T):
    result = ''
    R, S = input().split()
    for j in S:
        result += j*int(R)
    print(result)