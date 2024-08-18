import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

pairs = [5, 3, 4, 1, 2, 0]  # 마주보는 면 인덱스

max_sum = 0

for i in range(6):  # 첫 번째 주사위의 아랫면을 6가지로 설정
    sum_side = 0
    top = arr[0][pairs[i]]  # 첫 번째 주사위의 윗면

    for j in range(N):  # 모든 주사위를 쌓아가면서 처리
        bottom = top
        top_index = arr[j].index(bottom)
        top = arr[j][pairs[top_index]]

        # 현재 주사위의 옆면 중 최대값 더하기
        side_max = max([x for k, x in enumerate(arr[j]) if k not in [top_index, pairs[top_index]]])
        sum_side += side_max

    max_sum = max(max_sum, sum_side)

print(max_sum)