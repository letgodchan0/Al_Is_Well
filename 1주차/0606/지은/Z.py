n, r, c = map(int, input().split())
visit = 0

#네 구역으로 나누어 r행 c열의 좌표가 어느 구역에 있는지 찾기
while n:
    n -= 1
    size = 2**n #사각형의 크기

    if r < size and c < size:       #제 1사분면
        visit += 0

    elif r < size and c >= size:    #제 2사분면
        visit += size * size
        c -= size
    
    elif r >= size and c < size:    #제 3사분면
        visit += size * size * 2
        r -= size

    else:                           #제 4사분면
        visit += size * size * 3
        r -= size

print(visit)