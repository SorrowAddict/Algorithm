import sys
input = sys.stdin.readline

def my_count(lst):
    COUNTS = [0] * 5
    for x in lst:
        COUNTS[x] += 1
    return COUNTS

N = int(input())
for _ in range(N):
    # 카운팅 정렬의 1단계 카운트 배열 생성 함수 활용
    A = my_count(list(map(int, input().split()))[1:])
    B = my_count(list(map(int, input().split()))[1:])

    # 4부터 1까지
    for i in range(4, 0, -1):
        if A[i] != B[i]:
            # A > B 이면 A 승리
            if A[i] > B[i]:
                print('A')
                break
            # A < B 이면 B 승리
            elif A[i] < B[i]:
                print('B')
                break
    else:   # 반복문 순회가 끝났음에도 승부가 안났다면 무승부 처리
        print('D')