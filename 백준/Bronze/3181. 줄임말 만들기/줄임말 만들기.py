lst = list(map(str, input().split()))
result = lst[0][0].title()
ignore_words = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
for i in lst[1:]:
    if i not in ignore_words:
        result += i[0].title()
print(result)