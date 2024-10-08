import sys
input = sys.stdin.readline

n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)]

min_v = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n]:
        min_v = 1
        break
    elif arr[n-i**2]:
        min_v = 2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]:
                min_v = 3
print(min_v)