import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    start, end = 0, x
    while start < end:
        mid = (start + end) // 2
        if (y + mid) * 100 // (x + mid) != z:
            end = mid
        else:
            start = mid + 1
    print(start)