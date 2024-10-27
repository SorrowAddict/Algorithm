import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
     A, B = map(int, input().split())
     print(f'Case #{i+1}: {A} + {B} = {A+B}\n')