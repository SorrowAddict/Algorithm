# 1003. 피보나치 함수

T = int(input())
for _ in range(T):
    N = int(input())
    v0, v1 = 1, 0
    for _ in range(N):
        v0, v1 = v1, v0+v1
    print(v0, v1)