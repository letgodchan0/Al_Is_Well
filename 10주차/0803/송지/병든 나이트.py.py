n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if 1 + (m - 1) // 2 >= 4:
        print(4)
    else:
        print(1 + (m - 1) // 2)
elif m <= 4:
    print(m)
elif 5 <= m <= 6:
    print(4)
else:
    print(m - 2)