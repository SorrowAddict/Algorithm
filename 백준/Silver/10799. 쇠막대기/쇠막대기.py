def my_len(lst):
    cnt_lst = 0
    for _ in lst:
        cnt_lst += 1
    return cnt_lst

arr = input()
result = 0
cnt = 0

for i in range(my_len(arr)):
    if i > 0:
        if arr[i] == '(':
            cnt += 1
        elif arr[i] == ')':
            cnt -= 1
        if arr[i] == ')' and arr[i-1] == '(':
            result += cnt
        elif arr[i] == ')' and arr[i-1] == ')':
            result += 1
    else:
        if arr[i] == '(':
            cnt += 1

print(result)