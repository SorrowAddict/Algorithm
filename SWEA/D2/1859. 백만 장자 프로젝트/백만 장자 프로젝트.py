# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:
            result += arr[i]-arr[i-1]
            arr[i-1] = arr[i]

    print(f'#{tc}', result)