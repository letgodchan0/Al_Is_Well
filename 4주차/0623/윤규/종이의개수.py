import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]


def paper(si, sj, n):
    global cm, cz, co
    if n == 1:
        if arr[si][sj] == -1:
            cm += 1
        elif arr[si][sj] == 0:
            cz += 1
        elif arr[si][sj] == 1:
            co += 1
    else:
        m = arr[si][sj]
        ch = 0
        for i in range(n):
            for j in range(n):
                if m == arr[si+i][sj+j]:
                    continue
                else:
                    ch = 1
                    break
            if ch == 1:
                break
        else:
            if num == -1:
                cm += 1
            elif num == 0:
                cz += 1
            elif num == 1:
                co += 1 
            return

        for i in range(3):
            for j in range(3):
                check = 0
                num = arr[si+i*(n//3)][sj+j*(n//3)]
                for l in range(n//3):
                    for k in range(n//3):
                        if arr[si+i*(n//3)+l][sj+j*(n//3)+k] == num:
                            continue
                        else:
                            check = 1
                            break
                    if check == 1:
                        paper(si+i*(n//3), sj+j*(n//3), n//3)
                        break

                else:
                    if num == -1:
                        cm += 1
                    elif num == 0:
                        cz += 1
                    elif num == 1:
                        co += 1
                

cm, cz, co = 0, 0, 0
paper(0, 0, n)
print(cm)
print(cz)
print(co)