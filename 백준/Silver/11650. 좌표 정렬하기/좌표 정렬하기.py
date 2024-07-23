import sys
input=sys.stdin.readline
n=int(input())
c=[]
for i in range(n):
    d,e=map(int,input().split())
    c.append(d*200001+e)
for i in sorted(c):
    print((i+100000)//200001,i-200001*((i+100000)//200001))