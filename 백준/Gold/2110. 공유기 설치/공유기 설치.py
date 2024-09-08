import sys
input = sys.stdin.readline

def bs(s, e):
    while s <= e:
        mid = (s + e) // 2

        start = arr[0]
        cnt = 1
        for i in arr:
            if start + mid < i:
                start = i
                cnt += 1
            if cnt >= C:
                s = mid + 1
                break
        if cnt >= C:
            s = mid + 1
        else:
            e = mid - 1
    print(s)


N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
start, end = 1, arr[-1]
bs(start, end)