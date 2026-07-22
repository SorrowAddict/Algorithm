def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        tmp = ''
        for x in s:
            if x in skill:
                tmp += x
        if tmp == skill[:len(tmp)]:
            answer += 1
    return answer