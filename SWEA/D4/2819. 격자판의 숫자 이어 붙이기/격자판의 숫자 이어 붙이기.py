dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시작점: 각 좌표
# 끝점: 문자열의 길이가 7이면 종료
def dfs(y, x, path):
    if len(path) == 7:
        result.add(path)    # 현재 까지의 경로를 결과 set 에 저장
        return

    # 상하좌우 확인하면서 갈 수 있으면 이동
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<4 and 0<=nx<4:
            dfs(ny, nx, path + arr[ny][nx]) # 문자열을 누적하면서 다음으로 이동

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc}', len(result))