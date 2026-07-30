def solution(order):
    answer = 0
    lst = []
    idx = 0
    
    for i in range(1, len(order) + 1):
        lst.append(i)
        while lst and lst[-1] == order[idx]:
            answer += 1
            idx += 1
            lst.pop()
    return answer