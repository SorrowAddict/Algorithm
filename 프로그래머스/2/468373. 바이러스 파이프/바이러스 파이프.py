from collections import deque

def solution(n, infection, edges, k):
    answer = 0
    
    arr = [[] for _ in range(n + 1)]
    
    for x, y, t in edges:
        arr[x].append((y, t))
        arr[y].append((x, t))
    
    def bfs(pipe_t, infected):
        s = set(infected)
        q = deque(list(infected))
        
        while q:
            i = q.popleft()
            for nxt, t in arr[i]:
                if pipe_t == t and nxt not in s:
                    q.append(nxt)
                    s.add(nxt)
        return s
    
    def dfs(level, infected):
        nonlocal answer
        
        if level == k:
            answer = max(answer, len(infected))
            return
        
        for pipe_t in [1, 2, 3]:
            s = bfs(pipe_t, infected)
            dfs(level + 1, s)
    dfs(0, {infection})
    return answer