N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i != 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            cnt += 1
print(cnt)