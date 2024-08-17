import sys
input = sys.stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x = w - abs(w - (x + t) % (2 * w))
y = h - abs(h - (y + t) % (2 * h))

print(x, y)