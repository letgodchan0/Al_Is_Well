n = int(input())
x_y = [list(map(int,input().split())) for _ in range(n)]
srtd_x_y = sorted(x_y, key=lambda x: (x[1], x[0]))
for co in srtd_x_y:
    print(*co)