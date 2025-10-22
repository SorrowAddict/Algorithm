import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, *arr = map(int, input().split())
    avg = sum(arr) / N
    cnt = sum(1 for x in arr if x > avg)
    print(f"{cnt / N * 100:.3f}%")