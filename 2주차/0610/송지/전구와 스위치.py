a = int(input())
com = [n for n in range(a)]

lst = list(map(int, input()))
ans_lst = list(map(int, input()))
btn = 100001

if lst[0] == ans_lst[0]:
    ans = [[0, 0], [1, 1]]
else:
    ans = [[1, 0], [0, 1]]

for b in ans:
    lst2 = lst.copy()

    for i in range(2):
        if b[i]:
            for j in [-1, 0, 1]:
                if 0 <= i + j < a and lst2[i + j]:
                    lst2[i + j] = 0
                elif 0 <= i + j < a and not lst2[i + j]:
                    lst2[i + j] = 1

    answer = sum(b)

    for i in range(1, a - 1):
        if lst2[i] != ans_lst[i]:
            for j in [0, 1, 2]:
                if 0 <= i + j < a and lst2[i + j]:
                    lst2[i + j] = 0
                elif 0 <= i + j < a and not lst2[i + j]:
                    lst2[i + j] = 1
            answer += 1

    if lst2 == ans_lst and answer < btn:
        btn = answer

if btn != 100001:
    print(btn)
else:
    print(-1)
