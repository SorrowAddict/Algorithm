X = int(input())
tmp = [64, 32, 16, 8, 4, 2, 1]
ans = 0
for t in tmp:
    if X >= t:
        X -= t
        ans += 1
    if X == 0:
        break
print(ans)