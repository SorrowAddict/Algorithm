import sys
input = sys.stdin.readline

files = [input().rstrip() for _ in range(int(input()))]
result = list(files[0])

for file in files[1:]:
    for i in range(len(file)):
        if result[i] != file[i]:
            result[i] = '?'

print(''.join(result))