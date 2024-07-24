S = input()
arr = [-1] * 26
for i in S:
    arr[ord(i)-97] = S.index(i)
print(*arr)