import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
cnt = 0

for i in range(N):
    target = A[i]
    left, right = 0, N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = A[left] + A[right]
        if current_sum == target:
            cnt += 1
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1
print(cnt)