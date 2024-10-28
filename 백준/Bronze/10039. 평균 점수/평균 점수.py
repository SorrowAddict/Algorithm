ans = 0
for _ in range(5):
    i = int(input())
    if i < 40:
        i = 40
    ans += i
print(int(ans / 5))