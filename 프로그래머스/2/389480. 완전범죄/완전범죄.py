def solution(info, n, m):
    answer = 1e9
    _level = len(info)
    visited = set()

    def dfs(a, b, level):
        nonlocal answer
        
        if level == _level:
            if a < n and b < m:
                answer = min(answer, a)
            return
        if a >= n or b >= m or a >= answer:
            return
        if (a, b, level) not in visited:
            visited.add((a, b, level))
        else:
            return
        
        dfs(a + info[level][0], b, level + 1)
        dfs(a, b + info[level][1], level + 1)
    
    dfs(0, 0, 0)
    
    if answer == 1e9:
        return -1
    else: return answer