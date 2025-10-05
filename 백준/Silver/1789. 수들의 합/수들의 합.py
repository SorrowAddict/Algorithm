N = int(input())
ans = 0
i = 1
while N >= i:
    N -= i
    ans += 1
    i += 1
print(ans)