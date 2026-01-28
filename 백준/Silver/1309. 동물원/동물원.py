# N = 0 -> 1
# N = 1 -> 1 + 2 = 3
# N = 2 -> 3 * 2 + 1 = 7
# N = 3 -> 7 * 2 + 3 = 17
# N = 4 -> 17 * 2 + 7 = 41

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, N + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
print(dp[N])