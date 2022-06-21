def find(ri, rj, bi, bj, cnt):
    global n, m, ans

    if cnt >= 10 or cnt >= ans:
        return

    ri1, rj1, bi1, bj1 = ri, rj, bi, bj

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ri, rj, bi, bj = ri1, rj1, bi1, bj1
        no = 0
        check = 0

        while True:  # R부터 옮길건데 B랑 부딪히면 check 해두고 나중에 또 옮길거임
            ni, nj = ri + di, rj + dj
            if ni == bi and nj == bj:
                check = 1
                break
            elif arr[ni][nj] == '.':
                ri, rj = ni, nj
            elif arr[ni][nj] == '#':
                break
            elif arr[ni][nj] == 'O':
                ri, rj = ni, nj
                break

        while True:  # B 옮김
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == '#' or (ni == ri and nj == rj and arr[ni][nj] != 'O'):
                break
            elif arr[ni][nj] == '.':
                bi, bj = ni, nj
            elif arr[ni][nj] == 'O':
                no = 1
                break

        if check:  # check 해뒀으면 R 다시 옮김
            while True:
                ni, nj = ri + di, rj + dj
                if arr[ni][nj] == '#' or (ni == bi and nj == bj):
                    break
                elif arr[ni][nj] == '.':
                    ri, rj = ni, nj
                elif arr[ni][nj] == 'O':
                    ri, rj = ni, nj
                    break

        if [ri1, rj1, bi1, bj1] == [ri, rj, bi, bj]:  # 옮긴게 그대로면 더 이상 보지 말자
            no = 1

        if arr[ri][rj] == 'O' and not no:  # R만 구멍에 잘 들어갔으면 리턴
            if cnt + 1 < ans:
                ans = cnt + 1
            return

        if not no:  # 문제되는거 없으면 재귀
            find(ri, rj, bi, bj, cnt + 1)


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = 11

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'

find(ri, rj, bi, bj, 0)

if ans != 11:
    print(ans)
else:
    print(-1)
