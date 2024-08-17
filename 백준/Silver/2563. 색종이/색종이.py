import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x-1+i][y-1+j] = 1
    
result = 0
for x in arr:
    result += sum(x)
print(result)