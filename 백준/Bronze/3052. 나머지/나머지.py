lst = []
for i in range(10):
    x = int(input())
    lst.append(x%42)
print(len(list(set(lst))))