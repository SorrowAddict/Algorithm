from math import factorial as f
N, K = map(int, input().split())
print(int(f(N)/(f(K)*f(N-K))))