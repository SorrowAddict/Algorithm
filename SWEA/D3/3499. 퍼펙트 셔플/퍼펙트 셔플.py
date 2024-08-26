# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    card = input().split()  # A B C D E F
    deck = [0]*N

    d = (N+1)//2        # 아래오는 카드 시작 N//2 + N%2

    i1 = 0
    i2 = d
    i3 = 0  # 새로 만들 덱
    while i3 < N:   # 셔플이 끝나기 전이면
        if i1 < d:
            deck[i3] = card[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = card[i2]
            i2 += 1
            i3 += 1

    print(f'#{tc}', *deck)