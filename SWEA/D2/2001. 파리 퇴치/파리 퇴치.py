# 2001. 파리 퇴치

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            temp = 0
            for k in range(M):
                temp += sum(arr[i+k][j:j+M])
            if result < temp:
                result = temp

    print(f'#{tc}', result)