import sys
input = sys.stdin.readline

# 초기 빙고판 입력
arr = [list(map(int, input().split())) for _ in range(5)]

def check_bingo():
    count = 0

    # 대각선 체크
    if all(arr[i][i] == 0 for i in range(5)):
        count += 1
    if all(arr[i][4-i] == 0 for i in range(5)):
        count += 1

    # 가로 체크
    for i in range(5):
        if all(arr[i][j] == 0 for j in range(5)):
            count += 1

    # 세로 체크
    for j in range(5):
        if all(arr[i][j] == 0 for i in range(5)):
            count += 1

    return count

# 빙고 수 확인 리스트 입력
lst = []
for _ in range(5):
    lst.extend(map(int, input().split()))

cnt = 0
for x in lst:
    cnt += 1
    for i in range(5):
        for j in range(5):
            if arr[i][j] == x:
                arr[i][j] = 0
                break
        else:
            continue
        break

    if check_bingo() >= 3:
        print(cnt)
        break