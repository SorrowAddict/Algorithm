def my_max(lst):
    max_v = lst[0]
    for x in lst:
        if max_v < x:
            max_v = x
    return [max_v, lst.index(max_v)]

def my_min(lst):
    min_v = lst[0]
    for x in lst:
        if min_v > x:
            min_v = x
    return [min_v, lst.index(min_v)]

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    dump_tri = int(input())
    arr = list(map(int, input().split()))

    while dump_tri > 0:
        arr[my_max(arr)[1]] -= 1
        arr[my_min(arr)[1]] += 1
        dump_tri -= 1

    print(f'#{tc} {my_max(arr)[0] - my_min(arr)[0]}')