s = input()
num = []
giho = []
j = 0

for i in s:
    if i == '+' or i == '-':
        giho.append(i)
        j += 1
    else:
        if len(num) > j:
            num[j] += i
        else:
            num.append(i)

ans = int(num[0].lstrip('0'))

for i in range(len(giho)):
    if giho[i] == '-':
        for j in range(i + 1, len(giho)):
            if giho[j] == '+':
                giho[j] = '-'
            else:
                break

for i in range(len(giho)):
    if giho[i] == '+':
        ans += int(num[i + 1].lstrip('0'))
    else:
        ans -= int(num[i + 1].lstrip('0'))

print(ans)
