# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    lst = input().split('0')

    result = 0
    for x in lst:
        result = max(result, len(x))

    print(f'#{tc}', result)