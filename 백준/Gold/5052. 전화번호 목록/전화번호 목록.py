import sys
input = sys.stdin.readline

def check():
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            print('NO')
            break
    else: print('YES')
    return

for _ in range(int(input())):
    n = int(input())
    arr = list(input().strip() for _ in range(n))
    arr.sort()
    check()