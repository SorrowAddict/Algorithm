import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(n-1):
    dp[i+1] = max(dp[i+1], dp[i] + dp[i+1])
print(max(dp))