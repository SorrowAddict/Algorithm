# Testcase 수
T = 10

# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    result = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8-length+1):
            # print(arr[i][j:j+length], list(reversed(arr[i][j:j+length])))
            if arr[i][j:j+length] == list(reversed(arr[i][j:j+length])):
                result += 1

    # 세로 탐색
    for j in range(8):
        for i in range(8-length+1):
            check = "".join([arr[i + k][j] for k in range(length)])
            if check == check[::-1]:
                result += 1

    print(f'#{tc}', result)