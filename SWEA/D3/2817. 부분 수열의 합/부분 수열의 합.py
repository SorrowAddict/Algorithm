# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    # 모든 부분 집합의 경우의 수
    for i in range(1<<N):
        temp = 0
        # 찾아볼 모든 인덱스 i 값
        for j in range(len(arr)):
            if i & (1<<j):
                temp += arr[j]
        if temp == K:
            result += 1
    print(f'#{tc}', result)