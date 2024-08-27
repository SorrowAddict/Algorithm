def inorder_traversal(node):
    if node:
        if len(left[node]) == 2:
            inorder_traversal(left[node][1])
        print(left[node][0], end='')
        if len(right[node]) == 2:
            inorder_traversal(right[node][1])

for tc in range(1, 11):
    N = int(input())    # 정점의 총 수
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        num, *arr = input().split()
        num = int(num)
        left[num], right[num] = [arr[0]], [arr[0]]
        for i in range(1, len(arr)):
            if i%2 == 1:
                left[num] = [arr[0], int(arr[i])]
            else:
                right[num] = [arr[0], int(arr[i])]
    root = 1
    print(f'#{tc}', end=' ')
    inorder_traversal(root)
    print()