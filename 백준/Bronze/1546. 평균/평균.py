N = int(input())
score = list(map(int, input().split()))

max_score = max(score)
mean_score = []

for _ in score:
    mean_score.append(_/max_score*100)
print(sum(mean_score)/N)