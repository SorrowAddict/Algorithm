d = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for x in arr:
        for i in range(len(x), 0, -1):
            if x[i-1] == '1':
                lst = x[i-56:i]
                lst = [d[lst[i:i + 7]] for i in range(0, len(lst), 7)]
                break
        else:
            continue
        break

    total, result = 0, 0
    for i, v in enumerate(lst):
        if i%2 == 0:
            total += int(v)*3
            result += int(v)
        else:
            total += int(v)
            result += int(v)
    else:
        if total%10 == 0:
            print(f'#{tc}', result)
        else:
            print(f'#{tc}', 0)