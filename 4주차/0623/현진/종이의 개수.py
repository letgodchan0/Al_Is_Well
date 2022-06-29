# Back_1780
import sys
input = sys.stdin.readline

# 1. 만약 종이가 모두 같은 수로 되어있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해 (1)의 과정을 반복한다.

def dfs(x, y, N):
    global minus, zero, plus

    check = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * N // 3, y + l * N // 3, N // 3)
                return
    
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus, zero, plus = 0, 0, 0

dfs(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')