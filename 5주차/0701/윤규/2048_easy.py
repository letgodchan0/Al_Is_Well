from copy import deepcopy
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]
maxV = 0

def move(arr, d):
    
    # 아래
    if d == 0:
        for j in range(n):
            z = n-1
            for i in range(n-2, -1, -1):
                tmp = arr[i][j]
                if tmp:
                    if arr[z][j] == 0:
                        arr[z][j] = tmp
                        arr[i][j] = 0
                    elif arr[z][j] == tmp:
                        arr[z][j] = tmp * 2
                        arr[i][j] = 0
                        z -= 1
                    else:
                        z -= 1
                        arr[i][j] = 0
                        arr[z][j] = tmp
    # 위
    if d == 1:
        for j in range(n):
            z = 0
            for i in range(1, n):
                tmp = arr[i][j]
                if tmp:
                    if arr[z][j] == 0:
                        arr[z][j] = tmp
                        arr[i][j] = 0
                    elif arr[z][j] == tmp:
                        arr[z][j] = tmp * 2
                        arr[i][j] = 0
                        z += 1
                    else:
                        z += 1
                        arr[i][j] = 0
                        arr[z][j] = tmp
    # 오른
    if d == 2:
        for i in range(n):
            z = n-1
            for j in range(n-2, -1, -1):
                tmp = arr[i][j]
                if tmp:
                    if arr[i][z] == 0:
                        arr[i][z] = tmp
                        arr[i][j] = 0
                    elif arr[i][z] == tmp:
                        arr[i][z] = tmp * 2
                        arr[i][j] = 0
                        z -= 1
                    else:
                        z -= 1
                        arr[i][j] = 0
                        arr[i][z] = tmp
    # 왼
    if d == 3:
        for i in range(n):
            z = 0
            for j in range(1, n):
                tmp = arr[i][j]
                if tmp:
                    if arr[i][z] == 0:
                        arr[i][z] = tmp
                        arr[i][j] = 0
                    elif arr[i][z] == tmp:
                        arr[i][z] = tmp * 2
                        arr[i][j] = 0
                        z += 1
                    else:
                        z += 1
                        arr[i][j] = 0
                        arr[i][z] = tmp
    return arr


def change(arr, cnt):
    global maxV
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                maxV = max(maxV, arr[i][j])

        return
    
    for i in range(4):
        new_arr = move(deepcopy(arr), i)
        change(new_arr, cnt+1)

change(arr, 0)

print(maxV)




# from copy import deepcopy

# n = int(input())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# print(graph)
# def move(board, dir):
#     if dir == 0:  # 동쪽
#         for i in range(n):
#             top = n - 1
#             for j in range(n - 2, -1, -1):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     board[i][j] = 0
#                     if board[i][top] == 0:
#                         board[i][top] = tmp
#                     elif board[i][top] == tmp:
#                         board[i][top] = tmp * 2
#                         top -= 1
#                     else:
#                         top -= 1
#                         board[i][top] = tmp

#     elif dir == 1:  # 서쪽
#         for i in range(n):
#             top = 0
#             for j in range(1, n):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     board[i][j] = 0
#                     if board[i][top] == 0:
#                         board[i][top] = tmp
#                     elif board[i][top] == tmp:
#                         board[i][top] = tmp * 2
#                         top += 1
#                     else:
#                         top += 1
#                         board[i][top] = tmp

#     elif dir == 2:  # 남쪽
#         for j in range(n):
#             top = n - 1
#             for i in range(n - 2, -1, -1):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     board[i][j] = 0
#                     if board[top][j] == 0:
#                         board[top][j] = tmp
#                     elif board[top][j] == tmp:
#                         board[top][j] = tmp * 2
#                         top -= 1
#                     else:
#                         top -= 1
#                         board[top][j] = tmp

#     else:
#         for j in range(n):
#             top = 0
#             for i in range(1, n):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     board[i][j] = 0
#                     if board[top][j] == 0:
#                         board[top][j] = tmp
#                     elif board[top][j] == tmp:
#                         board[top][j] = tmp * 2
#                         top += 1
#                     else:
#                         top += 1
#                         board[top][j] = tmp

#     return board


# def dfs(board, cnt):
#     global ans
#     if cnt == 5:
#         for i in range(n):
#             for j in range(n):
#                 ans = max(ans, board[i][j])
#         return

#     for i in range(4):
#         tmp_board = move(deepcopy(board), i)
#         dfs(tmp_board, cnt + 1)

# ans = 0
# dfs(graph, 0)
# print(graph)
# print(ans)