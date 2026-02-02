import sys
input = sys.stdin.readline

def find_parent(parent, target):
    if parent[target] != target:
        parent[target] = find_parent(parent, parent[target])
    return parent[target]

def union(parent, i, j):
    a = find_parent(parent, i)
    b = find_parent(parent, j)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
parent = {i: i for i in range(1, N + 1)}
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(parent, i + 1, j + 1)
plan = list(map(int, input().split()))
root = find_parent(parent, plan[0])
for city in plan:
    if find_parent(parent, city) != root:
        print("NO")
        break
else:
    print("YES")