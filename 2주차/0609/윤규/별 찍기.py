
# pypy 로는 되는데 python3 로는 시간초과 
n = int(input())

starlst = [['*'] * n for _ in range(n)]

blank = 1
while blank < n:
    for i in range(n):
        for j in range(n):
            if (i//blank)%3 == 1 and (j//blank)%3 == 1:
                starlst[i][j] = ' '
    blank *= 3 


for i in range(n):
    for j in range(n):
        print(starlst[i][j], end = '')
    print()



