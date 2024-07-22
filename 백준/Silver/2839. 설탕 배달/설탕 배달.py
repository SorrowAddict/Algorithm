n = int(input())
a =  n//5
s=0
imsi = n
for i in range(a+1):
    imsi = n - 5 * i
    if imsi%3 == 0:
        s = int(imsi/3+i)

if s == 0:
    print("-1")
else:
    print(s)