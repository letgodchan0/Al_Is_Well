ex = input().split('-')
for i in range(len(ex)):
    if i==0:
        ans = sum(list(map(int,(ex[i].split('+')))))
    else:
        ans -= sum(list(map(int,(ex[i].split('+')))))
print(ans)
