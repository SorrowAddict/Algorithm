N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())
ans_T = 0
for i in lst:
    ans_T += i//T +1
    if i%T == 0:
        ans_T -= 1
ans_P1 = N//P
ans_P2 = N%P
print(ans_T)
print(ans_P1, ans_P2)