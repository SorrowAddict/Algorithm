def recur(cnt, sum_height):
    global ans
    # 기저조건 가지치기. 이미 탑의 높이가 B 이상이라면, 더 이상 확인할 필요가 X
    if sum_height >= B:
        # B 이상인 탑 중 가장 낮은 것이 정답!
        ans = min(ans, sum_height)
        return

    # 기저조건: 모든 점원을 탑을 쌓는데 고려했는가?
    if cnt == N:
        return

    # cnt번 점원을 탑에 쌓는다
    recur(cnt + 1, sum_height + heights[cnt])
    # 안쌓는다
    recur(cnt + 1, sum_height)

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 1e9
    recur(0, 0)
    print(f'#{tc}', ans - B)