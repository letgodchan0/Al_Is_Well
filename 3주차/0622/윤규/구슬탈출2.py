from copy import deepcopy
import sys
sys.setrecursionlimit(2000000)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
d = [(1,0), (-1,0), (0,1), (0,-1)]  # 아래, 위, 오, 왼


def find(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'B':
                bi, bj = i, j
            if arr[i][j] == 'R':
                ri, rj = i, j
    return bi, bj, ri, rj

ma = max(n,m)
def end(i, arrr):
    arr = deepcopy(arrr)
    bi, bj, ri, rj = find(arr)

    di, dj = d[i]
    for _ in range(ma):
        checkA = 1
        checkB = 1
        checkO = 0
        ni, nj = ri + di, rj + dj
        nbi, nbj = bi + di, bj + dj
        if checkA:
            if arr[ni][nj] == '#':
                checkA = 0
            elif arr[ni][nj] == 'B':
                if checkB == 0:
                    break
                
            elif arr[ni][nj] == '.':
                arr[ri][rj] = '.'
                ri, rj = ni, nj
                arr[ri][rj] = 'R'
            elif arr[ni][nj] == 'O':
                checkA = 0
                if checkB == 0:
                    return 1
                else:
                    arr[ri][rj] = '.'
                    checkO = 1
        
                    
        if checkB:
            if arr[nbi][nbj] == '#':
                checkB = 0
            elif arr[nbi][nbj] == 'R':
                if checkA == 0:
                    break
                
            elif arr[nbi][nbj] == '.':
                arr[bi][bj] = '.'
                bi, bj = nbi, nbj
                arr[bi][bj] = 'B'
            elif arr[nbi][nbj] == 'O':
                
                return -1
    if checkO:
        return 1
    # for i in range(n):
    #     for j in range(m):
    #         print(arr[i][j], end='')
    #     print()
    # print('ㅡㅡㅡㅡㅡㅡㅡ')
    # print(di, dj)
    return arr

        
def search(i, s, k):
    global cnt

    if i > 10:
        return 
    if s == -1:
        return
    if i >= cnt:
        return

    if s == 1:
        if i < cnt:
            cnt = i
            return


    
    for j in range(3,-1,-1):
        
        new_arr = end(j, s)
        if i == 0:
            search(i+1, new_arr, j)
        elif i != 0 :
            if (k == 0 or k == 1) and (j==3 or j==2):
                search(i+1, new_arr, j)
            elif (k == 2 or k == 3) and (j==0 or j==1):
                search(i+1, new_arr, j)
    
            
cnt = 11
search(0, arr, -1)
if cnt == 11:
    print(-1)
else:
    print(cnt)



# arr1=end(3, arr)
# arr1=end(0, arr)
# arr1=end(2, arr)
# print(arr)