import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.append(int(input()))

print(*sorted(l, reverse=True), sep='\n')