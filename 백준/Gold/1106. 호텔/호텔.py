import sys
input = sys.stdin.readline

C, N = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [1e7 for _ in range(C + 100)]
dp[0] = 0

for cost, customer in costs:
    for i in range(customer, C + 100):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))