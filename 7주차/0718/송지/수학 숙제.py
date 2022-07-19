n = int(input())
lst = []

for _ in range(n):
    a = input()
    num = ''
    for i in range(a):
        if i.isdigit():
            num += i
        elif num:
            lst.append(int(num))
            num = ''
    if num:
        lst.append(int(num))
        
for i in lst.sort():
    print(i)