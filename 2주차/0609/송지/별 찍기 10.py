a = int(input())

lst = [['*'] * a for _ in range(a)]

now = 1

while now < a:
    for i in range(a):
        for j in range(a):
            if (i // now) % 3 == 1 and (j // now) % 3 == 1:
                lst[i][j] = ' '
    now *= 3

for i in range(a):
    for j in range(a):
        print(lst[i][j], end='')
    print('')
