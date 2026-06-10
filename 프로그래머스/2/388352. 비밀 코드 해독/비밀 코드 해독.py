def solution(n, q, ans):
    answer = 0
    s_q = [set(x) for x in q]
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j + 1)
        if len(subset) != 5:
            continue
        
        s_subset = set(subset)
        for s, target in zip(s_q, ans):
            cnt = len(s & s_subset)
            if cnt != target:
                break
        else:
            answer += 1
    return answer