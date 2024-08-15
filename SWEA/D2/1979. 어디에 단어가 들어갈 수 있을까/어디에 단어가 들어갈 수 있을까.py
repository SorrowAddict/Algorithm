# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        row, col = 0, 0
        for j in range(N):
            if arr[i][j] == 1:
                row += 1
            else:
                if row == K:
                    result += 1
                row = 0
            if arr[j][i] == 1:
                col += 1
            else:
                if col == K:
                    result += 1
                col = 0
        if row == K:
            result += 1
        if col == K:
            result += 1

    print(f'#{tc}', result)