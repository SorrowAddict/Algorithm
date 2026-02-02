import sys
input = sys.stdin.readline

def find_parent(parent, target):
    if parent[target] != target:
        parent[target] = find_parent(parent, parent[target])
    return parent[target]

N = int(input())
M = int(input())
parent = {i: i for i in range(1, N + 1)}
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            a = find_parent(parent, i + 1)
            b = find_parent(parent, j + 1)
            if a != b:
                parent[b] = a
plan = list(map(int, input().split()))
root = find_parent(parent, plan[0])
plan_parents = set(find_parent(parent, city) for city in plan)
print("YES" if len(plan_parents) == 1 else "NO")