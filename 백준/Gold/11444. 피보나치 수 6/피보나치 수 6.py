import sys
input = sys.stdin.readline

def fibonaci(n):
    if n <= 2:
        return d[n]
    if d.get(n) == None:
        if n % 2 == 0:
            temp1 = fibonaci(n//2)
            temp2 = fibonaci(n//2-1)
            temp3 = temp1 + temp2
            d[n] = (temp1 * (temp2 + temp3)) %1000000007
            return d[n]
        elif n % 2 == 1:
            temp1 = fibonaci(n//2)
            temp2 = fibonaci(n//2+1)
            d[n] = (temp1**2 + temp2**2) %1000000007
            return d[n]
    else:
        return d[n]

n = int(input())
d = dict()
d[0], d[1], d[2] = 0, 1, 1
print(fibonaci(n))