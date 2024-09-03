def change_nums(nums, cnt):
    global max_v
    global visited

    value = int(''.join(nums))
    if value in used[cnt]:
        return
    used[cnt].add(value)

    if cnt == count:
        max_v = max(max_v, value)
        return

    for i in range(l):
        for j in range(i+1, l):
            nums[i], nums[j] = nums[j], nums[i]
            change_nums(nums, cnt +1)
            nums[i], nums[j] = nums[j], nums[i]

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    nums, count = input().split()
    nums = list(nums)
    count = int(count)
    l = len(nums)

    max_v = 0
    used = [set() for _ in range(count+1)]
    change_nums(nums, 0)

    print(f'#{tc}', max_v)