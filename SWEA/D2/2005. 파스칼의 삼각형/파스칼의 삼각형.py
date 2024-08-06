# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    print(f'#{tc}')

    N = int(input())
    arr = [[] for _ in range(11)]

    for i in range(1, N+1):
        if i == 1 or i == 2:
            arr[i] = [1] * i
        else:
            value = []
            for idx, v in enumerate(arr[i-1]):
                if 0 <= idx < len(arr[i-1])-1:
                    value.append(arr[i-1][idx]+arr[i-1][idx+1])
            arr[i] = [1, *value, 1]
        print(*arr[i])