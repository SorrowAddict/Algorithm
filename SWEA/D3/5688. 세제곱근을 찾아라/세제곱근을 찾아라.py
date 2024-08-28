# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    ans = -1
    temp = round(N ** (1/3))
    if N == temp**3:
        ans = temp

    print(f'#{tc}', ans)