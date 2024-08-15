T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]

    # 흑돌 1 백돌 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1

    # 상하좌우대각선
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for _ in range(M):
        # 입력받고 좌표-1씩해서 변환해 알맞은 위치에 돌 놓기
        i, j, color = map(int, input().split())
        i -= 1
        j -= 1
        board[i][j] = color

        for direction in range(8):
            need_to_change_color = []
            distance = 1
            while 0 <= i + dx[direction] * distance < N and 0 <= j + dy[direction] * distance < N:
                x = i + dx[direction] * distance
                y = j + dy[direction] * distance
                # 해당 방향이 빈칸이면 더 계산할 필요 없음
                if board[x][y] == 0:
                    break

                # 해당 방향이 같은 색이면 사이에 있는 애들 전부 색깔 변환
                if board[x][y] == color:
                    for each_x, each_y in need_to_change_color:
                        board[each_x][each_y] = color
                    break

                # 이도저도 아니면 일단 색깔바꿀 생각하고 다음칸 탐색하기
                need_to_change_color.append([x, y])

                distance += 1

    # 칸수 세기
    cnt_black = 0
    cnt_white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_black += 1
            if board[i][j] == 2:
                cnt_white += 1
    print(f'#{tc} {cnt_black} {cnt_white}')