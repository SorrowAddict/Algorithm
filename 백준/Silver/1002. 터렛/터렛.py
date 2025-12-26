import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    tmp = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif tmp > r1 + r2 or tmp < abs(r1 - r2):
        print(0)
    elif tmp == r1 + r2 or tmp == abs(r1 - r2):
        print(1)
    else:
        print(2)