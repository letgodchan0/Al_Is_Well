# 별 찍기 - 10
def draw_star(n):
    global map

    if n == 3:
        map[0][:3] = map[2][:3] = [1] * 3
        map[1][:3] = [1, 0, 1]
        return 
    a = n // 3
    draw_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                map[a*i+k][a*j:a*(j+1)] = map[k][:a]

N = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]

draw_star(N)
for i in map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()