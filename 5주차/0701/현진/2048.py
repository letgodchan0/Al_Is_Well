# Back_12100
import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# UP
def up(board):
    for j in range(N):
        pointer = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수 0이라면
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

# DOWN
def down(board):
    for j in range(N):
        pointer = N - 1
        for i in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수 0이라면
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

# LEFT
def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0이라면
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                # 포인터가 가리키는 수가 현재 위치의 수가 같을 때
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                # 포인터가 가리키는 수가 현재 위치의 수와 다를 때
                else:
                    pointer += 1
                    board[i][pointer] = tmp
    return board

# RIGHT
def right(board):
    for i in range(N):
        pointer = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0이라면
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                # 포인터가 가리키는 수가 현재 위치의 수와 같다면
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                # 포인터가 가리키는 수가 현재 위치의 수와 다르다면
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, board))
    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야한다.
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))

print(dfs(board, 0))