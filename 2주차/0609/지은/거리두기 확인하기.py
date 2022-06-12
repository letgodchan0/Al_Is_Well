def solution(places):
    answer = []
    for place in places:
        flag = 0
        for x in range(5):
            for y in range(5):
                if place[x][y]=="P":
                    if (x > 0 and place[x-1][y] == 'P') or  (x < 4 and place[x+1][y] == 'P') or (y > 0 and place[x][y-1] == 'P') or (y < 4 and place[x][y+1] == 'P'):
                    #응시자 주변에 응시자가 있을 때
                        flag = 1
                        break
                    if ((x > 1 and place[x-2][y] == 'P') and (place[x-1][y] != 'X')) or ((x < 3 and place[x+2][y] == 'P') and (place[x+1][y] != 'X')) or ((y > 2 and place[x][y-2] == 'P') and (place[x][y-1] != 'X')) or ((y < 3 and place[x][y+2] == 'P') and (place[x][y+1] != 'X')):
                    #맨해튼 거리 2이고(직선) 사이에 파티션이 없을 때
                        flag = 1
                        break
                    if ((x> 0 and y>0 and place[x-1][y-1] == 'P') and (place[x-1][y] != 'X' or place[x][y-1] != 'X')) or ((x< 4 and y<4 and place[x+1][y+1] == 'P') and (place[x+1][y] != 'X' or place[x][y+1] != 'X')) or ((x>0 and y<4 and place[x-1][y+1] == 'P') and (place[x-1][y] != 'X' or place[x][y+1] != 'X')) or ((x<4 and y>0 and place[x+1][y-1] == 'P') and (place[x+1][y] != 'X' or place[x][y-1] != 'X')):
                    #맨해튼 거리 2이고(대각선) 사이에 파티션이 없을 때
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 1:
            answer.append(0)
        else:   #잘 지켰을 때
            answer.append(1)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

#P 응시자. O 빈 테이블. X 파티션