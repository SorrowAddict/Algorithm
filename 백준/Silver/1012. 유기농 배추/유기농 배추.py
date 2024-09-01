# 1012. 유기농 배추

import sys
from collections import deque
input = sys.stdin.readline

def bfs(ti, tj):
    global cnt
    cnt += 1
    q = deque([(ti, tj)])
    arr[ti][tj] = 0
    # 인접한 배열에서만 bfs 탐색을 마치고 종료
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = 0

# 테스트 케이스
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    # 방문 유무를 체크할 리스트
    visited = [[0] * M for _ in range(N)]
    stack = []
    # 배추가 심어진 위치 큐에 push, arr에 표시
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
        stack.append((i, j))

    cnt = 0
    while stack:
        i, j = stack.pop()
        if arr[i][j] == 1:
            # 방문하지 않은 영역일 때만
            bfs(i, j)  # bfs 탐색
    print(cnt)