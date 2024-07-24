N = int(input())
lst = []

for i in range(N):
    lst.append(input())
print('\n'.join(sorted(list(set(lst)), key= lambda i: (len(i), i))))