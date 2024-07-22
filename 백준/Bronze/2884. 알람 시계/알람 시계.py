H, M = map(int, input().split())
if M-45 < 0:
    if H-1 < 0:
        print(H-1+24, M-45+60)
    else:
        print(H-1, M-45+60)
else:
    print(H, M-45)