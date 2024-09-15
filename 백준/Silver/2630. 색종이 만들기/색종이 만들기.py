import sys
input = sys.stdin.readline

def recur(y, x, n):
    color = paper[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != paper[i][j]:
                m = n // 2
                recur(y, x, m)
                recur(y, x + m, m)
                recur(y + m, x, m)
                recur(y + m, x + m, m)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]
recur(0, 0, N)
print(result[0])
print(result[1])