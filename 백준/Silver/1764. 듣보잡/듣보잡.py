import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cant_hear = set(input().replace('\n', '') for _ in range(N))
cant_see = set(input().replace('\n', '') for _ in range(M))

result = sorted(list(cant_hear & cant_see))

print(len(result))
print(*result, sep= '\n')