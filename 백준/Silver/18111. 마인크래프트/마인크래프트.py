import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v, max_v = min(map(min, arr)), max(map(max, arr))

ans = int(1e9), 0
for v in range(min_v, max_v+1):
    remove, add = 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > v:
                remove += arr[i][j]-v
            else:
                add += v-arr[i][j]
    if B+remove-add >= 0:
        # ans = min(ans, (remove*2 + add, v))
        time = remove*2 + add
        if time <= ans[0]:
            ans = time, v
print(*ans)