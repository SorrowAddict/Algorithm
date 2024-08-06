N = 1000 - int(input())

coin_types = [500, 100, 50, 10, 5, 1]

cnt = 0
for x in coin_types:
    cnt += N//x
    N %= x
print(cnt)