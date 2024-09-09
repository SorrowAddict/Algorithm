T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    if B < 2 or C < 3:      # A < B < C 구조를 만들 수 없는 케이스를 처리
        print(f'#{tc} -1')
        continue

    eat = 0     # 먹은 사탕 개수
    if B >= C:
        eat += B - (C - 1)
        B = C - 1
    if A >= B:
        eat += A - (B - 1)
        A = B - 1
    print(f'#{tc} {eat}')