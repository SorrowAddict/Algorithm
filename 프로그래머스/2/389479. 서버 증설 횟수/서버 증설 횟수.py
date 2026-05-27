def solution(players, m, k):
    answer = 0
    n = len(players)
    servers = [0] * (n + k)
    
    for i in range(n):
        tmp = players[i] // m
        if servers[i] < tmp:
            tmp2 = tmp - servers[i]
            answer += tmp2
            for j in range(i, i + k):
                servers[j] += tmp2
    return answer