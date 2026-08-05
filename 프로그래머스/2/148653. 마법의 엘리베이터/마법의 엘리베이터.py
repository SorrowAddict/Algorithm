def solution(storey):
    answer = 0
    
    while storey > 0:
        tmp1 = storey % 10
        tmp2 = (storey // 10) % 10
        
        if tmp1 > 5 or (tmp1 == 5 and tmp2 >= 5):
            answer += (10 - tmp1)
            storey = (storey + 10 - tmp1) // 10
        else:
            answer += tmp1
            storey //= 10
    return answer