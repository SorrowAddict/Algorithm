import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()  # 1 <= p <= 100,000
    n = int(input())

    arr_input = input().strip().strip('[]')
    if arr_input:
        arr = deque(map(int, arr_input.split(',')))
    else:
        arr = deque()

    is_reverse = 0
    for x in p:
        if x == 'R':
            is_reverse ^= 1
        elif x == 'D':
            if not arr:
                print('error')
                break
            if is_reverse:
                arr.pop()
            else:
                arr.popleft()
    else:
        if not is_reverse:
            print(str(list(arr)).replace(' ', ''))
        else:
            print(str(list(arr)[::-1]).replace(' ', ''))