import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

nums_counter = Counter(nums)
result = [nums_counter[check] for check in checks]
print(' '.join(map(str, result)))