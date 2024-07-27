N = int(input())
num_ans = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))
    num_ans = sum(num)+i
    if num_ans == N:
        print(i)
        break
    elif i == N:
        print(0)