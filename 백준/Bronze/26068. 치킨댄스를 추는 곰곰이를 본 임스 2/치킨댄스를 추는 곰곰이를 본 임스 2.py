N = int(input())
li = []; cnt = 0
for i in range(N):
    li.append(input()[2:])
    li[i] = int(li[i])
    if li[i] <= 90:
        cnt += 1
print(cnt)