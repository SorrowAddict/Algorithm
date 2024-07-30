A, B = map(int, input().split())
C = int(input())
time = A * 60 + B + C
if time < 1440:
    print(time//60, time%60)
else:
    time -= 1440
    print(time//60, time%60)