import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = []
for idx, x in enumerate(nums):
    result.insert(x, idx+1)

print(*result[::-1])