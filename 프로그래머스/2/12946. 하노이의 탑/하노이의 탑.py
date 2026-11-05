def hanoi(s, e, m, n, answer):
    if n == 1:
        answer.append([s, e])
    else:
        hanoi(s, m, e, n - 1, answer)
        hanoi(s, e, m, 1, answer)
        hanoi(m, e, s, n - 1, answer)
    return answer

def solution(n):
    answer = hanoi(1, 3, 2, n, [])
    return answer