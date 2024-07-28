L = int(input())
w = input()

result = 0
for i in range(0, L):
    result += (ord(w[i])-96)*(31**i)
print(result%1234567891)