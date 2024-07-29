N, K = map(int, input().split())
lst = [[0, 0] for i in range(6)]
for i in range(N):
    S, Y = map(int, input().split())
    lst[Y-1][S] += 1

cnt = 0
for case in lst:
    for i in case:
        cnt += i//K
        if i % K:
            cnt += 1
print(cnt)