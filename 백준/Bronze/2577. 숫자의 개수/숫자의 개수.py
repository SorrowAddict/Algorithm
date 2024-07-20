x = int(input())
y = int(input())
z = int(input())

k = str(x*y*z)

for i in range(10):
    print(k.count(str(i)))