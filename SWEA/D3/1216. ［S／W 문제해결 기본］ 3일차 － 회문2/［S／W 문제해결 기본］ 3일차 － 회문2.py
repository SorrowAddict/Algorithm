# Testcase 만큼 반복
for tc in range(1, 11):
    tc = input()
    # 100x100 배열 입력 받기
    arr = [input().strip() for _ in range(100)]
    max_v = 0

    # 가로 탐색
    for i in range(100):
        for length in range(2, 101):
            for j in range(100-length+1):
                if arr[i][j:j+length] == arr[i][j:j+length][::-1]:
                    max_v = max(max_v, length)

    # 세로 탐색
    for j in range(100):
        for length in range(2, 101):
            for i in range(100-length+1):
                check = ''.join(arr[k][j] for k in range(i, i+length))
                if check == check[::-1]:
                    max_v = max(max_v, length)

    print(f'#{tc}', max_v)