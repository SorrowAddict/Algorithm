def solution(targets):
    answer = 0
    targets.sort(key = lambda x: (x[1], x[0]))
    
    tmp = 0
    for s, e in targets:
        if s >= tmp:
            tmp = e
            answer += 1
    return answer