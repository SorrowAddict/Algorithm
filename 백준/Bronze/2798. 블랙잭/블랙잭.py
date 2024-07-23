N, M = map(int, input().split())
lst = list(map(int, input().split()))
my_max = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            my_sum = lst[i] + lst[j] + lst[k]
            if my_max < my_sum <= M:
                my_max = my_sum 
print(my_max)