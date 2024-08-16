N = int(input())
lst = [0] * 10000
for _ in range(N):
    lst[int(input())-1] += 1
for i, v in enumerate(lst):
    for _ in range(v):
        print(i+1)