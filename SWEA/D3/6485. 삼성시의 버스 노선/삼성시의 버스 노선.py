T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            counts[i] += 1

    P = int(input())
    lst = [int(input()) for _ in range(P)]

    print(f'#{tc}', end= ' ')
    for x in lst:
        print(counts[x], end= ' ')
    print()