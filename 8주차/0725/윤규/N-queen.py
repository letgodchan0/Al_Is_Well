def queen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    else:
        for j in range(n):
            if v1[j] == v2[j+i] == v3[j-i] == 0:    # 세로 피하기
                v1[j] = v2[j+i] = v3[j-i] = 1
                queen(i+1)
                v1[j] = v2[j+i] = v3[j-i] = 0



n = int(input())
cnt = 0
v1 = [0] * n
v2 = [0] * 2 * n
v3 = [0] * 2 * n
queen(0)
print(cnt)
