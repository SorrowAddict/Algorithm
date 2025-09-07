import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N) :
  tmp = input().strip()
  if tmp == 'P=NP' :
    print('skipped')
  else :
    a, b = map(int, tmp.split('+'))
    print(a + b)