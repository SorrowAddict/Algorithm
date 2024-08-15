# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            counts[i] += 1

    lst = []
    for _ in range(int(input())):
        lst.append(counts[int(input())])
    print(f'#{tc}', *lst)