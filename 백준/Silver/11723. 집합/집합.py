import sys

input = sys.stdin.readline

T = int(input())
S = set()

def add(x):
    S.add(x)

def remove(x):
    S.discard(x)

def check(x):
    if x in S:
        print(1)
    else: print(0)

def toggle(x):
    if x in S:
        S.discard(x)
    else:
        S.add(x)

def all():
    global S
    S = set([i for i in range(1, 21)])

def empty():
    global S
    S = set()

for tc in range(T):
    M = list(input().strip().split())
    F = M[0]
    if len(M) >= 2:
        num = int(M[1])
    if F == 'add':
        add(num)
    elif F == 'remove':
        remove(num)
    elif F == 'check':
        check(num)
    elif F == 'toggle':
        toggle(num)
    elif F == 'all':
        all()
    elif F == 'empty':
        empty()