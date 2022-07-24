def queen(x):
    global cnt
    if x == n:
        cnt += 1
        return

    for j in range(n):
        if v1[j] == v2[x+j] == v3[x-j] == 0:
            v1[j] = v2[x+j] =v3[x-j] = 1
            queen(x+1)
            v1[j] = v2[x+j] =v3[x-j] = 0

n = int(input())

cnt = 0
v1, v2, v3 = [0] * n, [0]*(2*n), [0]*(2*n)
queen(0)

print(cnt)