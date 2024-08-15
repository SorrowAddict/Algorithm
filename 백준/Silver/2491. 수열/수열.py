N = int(input())
arr = list(map(int, input().split()))

def check_max(a, b, v):
    v = max(max(a, b), v)
    return v if v > 2 else 2

max_v = 1
upper_cnt, lower_cnt = 1, 1
for i in range(1, N):
    if arr[i] > arr[i-1]:
        upper_cnt += 1
        lower_cnt = 1
    elif arr[i] < arr[i-1]:
        upper_cnt = 1
        lower_cnt += 1
    else:
        upper_cnt += 1
        lower_cnt += 1
    max_v = check_max(upper_cnt, lower_cnt, max_v)
print(max_v)