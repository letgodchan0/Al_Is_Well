def push():
    while coins:    
        x1, y1, x2, y2, cnt = coins.popleft()   #동전의 위치

        if cnt >= 10:   #10번 이상 움직임
            return -1
        
        for dx, dy in move:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy

            if nx1 in range(n) and ny1 in range(m) and nx2 in range(n) and ny2 in range(m): #범위 안에 존재
                if arr[nx1][ny1]=='#':  #벽을 만나면 이전 위치에 그대로
                    nx1, ny1 = x1, y1   
                if arr[nx2][ny2]=='#':  
                    nx2, ny2 = x2, y2  
                coins.append((nx1, ny1, nx2, ny2, cnt+1))
            elif nx1 in range(n) and ny1 in range(m):   #코인2가 떨어짐
                return cnt+1
            elif nx2 in range(n) and ny2 in range(m):   #코인1이 떨어짐
                return cnt+1 
            else:   #둘 다 떨어졌을 때
                continue
  

from collections import deque

arr = []
temp = []   #동전 위치 임시저장
move = [(0,1), (1,0), (0,-1), (-1,0)]
n, m = map(int, input().split())
coins = deque()  #동전의 좌표

for i in range(n):  #보드 정보 저장 o동전 .빈칸 #벽
    arr.append((list(input())))

    for j in range(m):  #동전의 위치 찾기
        if arr[i][j]=='o':
            temp.append(i)
            temp.append(j)

coins.append((*temp, 0))

print(push())