import sys
input = sys.stdin.readline

s = list(input().split())
t = list(input().split())

change = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        change = True
if change:
    print(1)
else:
    print(0)
    