def solution(n, q, ans):
    answer = 0
    s_q = [set(x) for x in q]
    
    subset = []
    def dfs(start, level):
        nonlocal answer
        
        if level == 5:
            s_subset = set(subset)
            for s, target in zip(s_q, ans):
                cnt = len(s & s_subset)
                if cnt != target:
                    return
            else: answer += 1
            return
        
        for i in range(start, n + 1):
            subset.append(i)
            dfs(i + 1, level + 1)
            subset.pop()
            
    dfs(1, 0)
    return answer