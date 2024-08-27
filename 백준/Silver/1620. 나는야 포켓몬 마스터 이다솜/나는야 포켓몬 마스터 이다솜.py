# 1620. 나는야 포켓몬 마스터

n, m = map(int, input().split())
d = dict()
d_v = dict()
for i in range(1, n+1):
    pokemon = input()
    d[i] = pokemon
    d[pokemon] = i
for _ in range(m):
    temp = input()
    if temp.isnumeric():
        print(d[int(temp)])
    else:
        print(d[temp])