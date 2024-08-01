# import sys

#  sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, 1, 0, -1]
    dj = [0, 1, 0, -1, 0]
    result = 0

    for i in range(N):
        for j in range(M):
            total = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    total += arr[ni][nj]
            if result < total:
                result = total

    print(f'#{tc}', result)