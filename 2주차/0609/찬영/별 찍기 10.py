def star(n):
    global arr

    if n == 3:
        arr[0][:3] = arr[2][:3] =[1] * 3
        arr[1][:3] = [1, 0, 1]
        return
    check = n // 3
    star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(check):
                arr[check*i+k][check*j:check*(j+1)] = arr[k][:check]

n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]
star(n)
for a in arr:
    for i in a:
        if i:
            print('*', end= '')
        else:
            print(' ', end= '')
    print()