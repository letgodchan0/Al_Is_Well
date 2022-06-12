d = [(0,1), (1,0), (-1,0), (0,-1)]

r, c = map(int, input().split())
arr = []
water_list = set()
rock_list = set()

def water(lis):
    new_water = set(lis)
    for wateri, waterj in lis:
        for di, dj in d:
            ni, nj = wateri + di, waterj + dj
            if 0<= ni < r and 0<= nj < c and arr[ni][nj] == '.':
                new_water.add((ni,nj))
                arr[ni][nj] = '*'
    return new_water

def gosum(lis, sec):
    pos_pos = set(lis)
    for gosi, gosj in lis:
        for di, dj in d:
            ni, nj = gosi + di, gosj + dj
            if 0<= ni < r and 0<= nj < c and arr[ni][nj] == 'D':
                return sec+1
            if 0<= ni < r and 0<= nj < c and arr[ni][nj] == '.' :
                pos_pos.add((ni,nj))
    return pos_pos

for i in range(r):
    row = list(map(str, input()))
    for j in range(c):
        if row[j] == 'D':
            Di, Dj = i, j
        elif row[j] == 'S':
            Si, Sj = i, j
        elif row[j] == '*' :
            water_list.add((i,j))
        elif row[j] == 'X':
            rock_list.add((i,j))
    arr.append(row)

pos_pos = [(Si, Sj)]

for i in range(r*c):
    # 물부터
    water_list = water(water_list)

    pos_pos = gosum(pos_pos, i)
    if pos_pos == i+1:
        print(pos_pos)
        break
else:
    print('KAKTUS')