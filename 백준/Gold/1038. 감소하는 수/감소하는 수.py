N = int(input())

def dfs(n):
    if len(n) > 10:
        return
    
    if n != '':
        ans.append(int(n))
    for i in range(10):
        if n == '' or int(n[-1]) > i:
            dfs(n + str(i))

ans = []
dfs('')
ans.sort()
if N >= len(ans):
    print(-1)
else:
    print(ans[N])