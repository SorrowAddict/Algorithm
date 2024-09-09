T = int(input())
result_l = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    start = max(A, C)
    end = min(B, D)

    result = end - start
    if result <= 0:
        result = 0
    result_l.append(result)
for idx, result in enumerate(result_l):
    print(f'#{idx + 1} {result}')