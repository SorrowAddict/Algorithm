def permutation():
    global ans
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if i & (1<<j):
                temp += arr[j]
        if temp == K:
            ans += 1

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    permutation()
    print(f'#{tc}', ans)