# 
sudo = [list(map(int, input().split(' '))) for _ in range(9)]
blank = []
num = [i for i in range(1,10)]

for i in range(9):
    for j in range(9):
        if sudo[i][j] == 0:
            blank.append((i,j))
print(blank)
# 빈칸이 한군데 인 곳 부터 채워나간다. 



print(sudo)