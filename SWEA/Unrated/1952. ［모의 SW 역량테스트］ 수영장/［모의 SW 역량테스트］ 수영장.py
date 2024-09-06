T = int(input())
for tc in  range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13
    dp[1] = min(days[1] * cost[0], cost[1])


    for i in range(1, 13):
        # 현재 달의 최소 비용을 계산
        # 이전 달 + 1일 권 구입 / 이전 달 + 1달 권 / 3달 전에 3달권 구입 중 최소
        dp[i] = min(dp[i-1] + days[i] * cost[0], dp[i-1] + cost[1])

        # index 오류를 피하기 위해, 3월 이후 계산을 따로 작성
        if i >= 3:
            # 1일권 vs 1달권 vs 3달권
            dp[i] = min(dp[i], dp[i-3] + cost[2])

    # 12월까지 계산 결과 vs 1년권
    result = min(dp[12], cost[3])
    print(f'#{tc} {result}')