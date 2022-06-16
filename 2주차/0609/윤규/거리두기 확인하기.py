# from itertools import combinations
def solution(places):

    answer = []
    for place in places:
        plst = []
        xlst = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    plst.append((i,j))
                elif place[i][j] == 'X':
                    xlst.append((i,j))
        
        
        for i in range(len(plst)):
            for j in range(i+1, len(plst)):
                # print( abs(plst[i][0] - plst[j][0]) + abs(plst[i][1] - plst[j][1]))
                if abs(plst[i][0] - plst[j][0]) + abs(plst[i][1] - plst[j][1]) == 1:
                    place = 0
                    break
                elif abs(plst[i][0] - plst[j][0]) + abs(plst[i][1] - plst[j][1]) == 2:
                    if plst[i][0] == plst[j][0]:
                        if (plst[i][0], (plst[i][1]+plst[j][1])/2) in xlst:
                            continue
                        else:
                            place = 0
                            break
                    elif plst[i][1] == plst[j][1]:
                        if ((plst[i][0]+plst[j][0])/2, plst[i][1]) in xlst:
                            continue
                        else:
                            place = 0
                            break
                    else:
                        if ((plst[i][0]+1,plst[i][1]) in xlst and (plst[i][0],plst[i][1]+1) in xlst) or ((plst[i][0]+1,plst[i][1]) in xlst and (plst[i][0],plst[i][1]-1) in xlst):
                            continue
                        else:
                            # print(i,j)
                            place = 0
                            break

            if place == 0:
                break

        if place != 0:
            place = 1
        answer.append(place)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))