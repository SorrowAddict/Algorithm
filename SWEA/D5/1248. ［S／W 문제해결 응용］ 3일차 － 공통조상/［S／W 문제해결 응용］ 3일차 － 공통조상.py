def parents(node, v1, v2):
    global cnt, temp_l, ans, check
    if node:
        cnt += 1
        # temp_l.append(node)
        parents(left[node], v1, v2)
        parents(right[node], v1, v2)
    if v1 == node:
        check += 1
    if v2 == node:
        check += 1

T = int(input())

for tc in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i + 1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    temp_l = []
    min_v = int(1e7)
    for root in range(1, V+1):
        cnt = 0
        ans = 0
        check = 0
        parents(root, v1, v2)
        if check == 2:
            temp_l.append([root, cnt])
    result = 0
    for x in temp_l:
        if min_v > x[1]:
            min_v = x[1]
            result = x[0]
    print(f'#{tc}',  result,min_v)