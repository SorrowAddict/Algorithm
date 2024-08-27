# 1620. 나는야 포켓몬 마스터

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
d_v = dict()
for i in range(1, n+1):
    pokemon = input().strip()
    d[pokemon] = i
    d[str(i)] = pokemon
for _ in range(m):
    temp = input().strip()
    print(d[temp])