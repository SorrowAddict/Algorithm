# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    A, B = input().split(' ')
    A = A.replace(B, ' ')
    print(f'#{tc}', len(A))