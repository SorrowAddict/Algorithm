def solution(plans):
    answer = []
    lst = []
    
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        plan[1] = h * 60 + m
        plan[2] = int(plan[2])
    
    plans.sort(key = lambda x: x[1])
    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        remain = plans[i + 1][1] - start
        
        if playtime <= remain:
            answer.append(name)
            remain -= playtime
            
            while lst and remain > 0:
                _name, _time = lst.pop()
                if _time <= remain:
                    answer.append(_name)
                    remain -= _time
                else:
                    lst.append((_name, _time - remain))
                    remain = 0
        else:
            lst.append((name, playtime - remain))
            
    answer.append(plans[-1][0])
    
    while lst:
        answer.append(lst.pop()[0])
    return answer