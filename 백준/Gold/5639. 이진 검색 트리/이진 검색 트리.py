import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def preorder_traversal(s, e):
    if s > e:
        return
    mid = e + 1
    for i in range(s+1, e+1):
        if arr[i] > arr[s]:
            mid = i
            break
    preorder_traversal(s+1, mid-1)
    preorder_traversal(mid, e)
    print(arr[s])

arr = []
while 1:
    try:
        arr.append(int(input()))
    except:
        break
preorder_traversal(0, len(arr)-1)