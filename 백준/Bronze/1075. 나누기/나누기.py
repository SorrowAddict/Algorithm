import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

N -= N % 100
for i in range(100):
    if (N + i) % F == 0:
        print(f"{i:02d}")
        break