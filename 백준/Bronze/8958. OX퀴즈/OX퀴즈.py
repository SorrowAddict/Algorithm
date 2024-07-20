N = int(input())

for i in range(N):
    reuslt = input()
    score = 0
    sumScore = 0
    for j in reuslt:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)