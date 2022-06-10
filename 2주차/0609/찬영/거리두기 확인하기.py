def find (i, j, place):
    for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
            # 바로 옆 또는 위 아래
            if ni == i or nj == j:
                return 0
            else:
                nii, njj = ni - i, nj - j
                if nii == -1 and njj == -1:
                    if place[ni+1][nj] == 'O' or place[ni][nj+1] == 'O':
                        return 0
                elif nii == 1 and njj == -1:
                    if place[ni-1][nj] == 'O' or place[ni][nj+1] == 'O':
                        return 0
                elif nii == -1 and njj == 1:
                    if place[ni][nj-1] == 'O' or place[ni+1][nj] == 'O':
                        return 0
                elif nii == 1 and njj == 1:
                    if place[ni-1][nj] == 'O' or place[ni][nj-1] == 'O':
                        return 0
        elif 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'O':
            if ni == i or nj == j:
                nii, njj = ni - i, nj - j
                if nii == -1 and 0 <= ni - 1 < 5 and place[ni-1][nj] == 'P':
                    return 0
                elif nii == 1 and 0 <= ni + 1 < 5 and place[ni+1][nj] == 'P':
                    return 0
                elif njj == -1 and 0 <= nj - 1 < 5 and place[ni][nj-1] == 'P':
                    return 0
                elif njj == 1  and 0 <= nj + 1 < 5 and place[ni][nj+1] == 'P':
                    return 0
                
    return 1

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not find(i, j, place):
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        # 거리두기 굳
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer