s = list(input())
t = list(input())
answer = 0

while t:
    if t[-1]=='A':
        del t[-1]
    else:   #t[-1]=='B'
        del t[-1]
        t = list(reversed(t))
    if s == t:
        answer = 1
        break

print(answer)