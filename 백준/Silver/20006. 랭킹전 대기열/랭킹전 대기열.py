import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().strip().split()
    l = int(l)
    if len(rooms) == 0:
        rooms.append([(l, n)])
        continue
    flag = True
    for i in range(len(rooms)):
        if len(rooms[i]) == m:
            continue
        if abs(rooms[i][0][0] - l) <= 10:
            rooms[i].append((l, n))
            flag = False
            break
    if flag:
        rooms.append([(l, n)])

for room in rooms:
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    for l, n in room:
        print(l, n)