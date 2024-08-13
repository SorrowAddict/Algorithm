from collections import deque

def create_pwd(lst):
    minus_value = 1
    while 1:
        temp = lst.popleft() - minus_value
        minus_value += 1
        if temp <= 0:
            temp = 0
            lst.append(temp)
            break
        if minus_value > 5:
            minus_value = 1
        lst.append(temp)
    return lst

# Testcase 만큼 반복
for _ in range(10):
    tc = int(input())
    arr = deque(list(map(int, input().split())))
    temp = 1e9

    print(f'#{tc}', *create_pwd(arr))