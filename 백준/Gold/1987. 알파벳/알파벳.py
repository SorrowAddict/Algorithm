import sys
input = sys.stdin.readline

def bfs():
    global max_cnt
    while q:
        x, y, tmp = q.pop()
        max_cnt = max(max_cnt, len(tmp))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] not in tmp:
                    q.add((nx, ny, tmp + arr[nx][ny]))
    return max_cnt

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
max_cnt = 1
q = set([(0, 0, arr[0][0])])
print(bfs())