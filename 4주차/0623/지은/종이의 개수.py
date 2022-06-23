def divide(x,y,m):
    global cnt
    if check(x,y,m):
        cnt[arr[x][y]+1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x+i*m//3, y+j*m//3, m//3)
    return

def check(x,y,m):   #다 같은 색으로 되어있는지
    tmp = arr[x][y]
    for i in range(m):
        for j in range(m):
            if tmp != arr[x+i][y+j]:
                return False
    return True

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = [0, 0, 0]   #-1, 0, 1
divide(0, 0, n)
print(*cnt, sep='\n')
