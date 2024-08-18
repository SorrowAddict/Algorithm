import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.append(int(input()))

for x in sorted(l):
    print(x)