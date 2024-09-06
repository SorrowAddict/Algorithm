def switch():
    cnt = 0
    for i in range(N):
        if A[i] != B[i]:
            for j in range(i, N):
                A[j] ^= 1
            cnt += 1
    return cnt

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{tc}', switch())