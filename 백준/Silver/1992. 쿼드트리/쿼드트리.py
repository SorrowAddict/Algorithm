import sys
input = sys.stdin.readline

def quad_tree(x, y, n):
    tmp = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != tmp:
                ans.append('(')
                half = n // 2
                quad_tree(x, y, half)
                quad_tree(x, y + half, half)
                quad_tree(x + half, y, half)
                quad_tree(x + half, y + half, half)
                ans.append(')')
                return
    ans.append(str(tmp))

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
ans = []
quad_tree(0, 0, N)
print(''.join(ans))