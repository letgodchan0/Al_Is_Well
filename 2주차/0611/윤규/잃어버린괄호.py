exp = input()
lst = []
mlst = []
num = ''
# -가 한번이라도 나왔어면 -1
check = 0
for i in exp:
    if i != '+' and i != '-':
        num += i
    else:
        rnum = int(num)
        num = ''
        if check == -1:
            mlst.append(rnum)

        else:
            lst.append(rnum)

    if i == '-':
        check = -1

rnum = int(num)
if check == -1:
    mlst.append(rnum)
elif check == 0:
    lst.append(rnum)

ans = sum(lst) - sum(mlst)

print(ans)