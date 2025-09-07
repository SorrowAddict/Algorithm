N = int(input())

for _ in range(N) :
  tmp = input()
  if tmp == 'P=NP' :
    print('skipped')
  else :
    a, b = map(int, tmp.split('+'))
    print(a + b)