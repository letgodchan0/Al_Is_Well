n = int(input())
lst = list(input())
check = len(lst)
for i in range(n - 1):
    b = list(input())
    for j in range(check):
        if lst[j] != b[j]:
            lst[j] = '?'
print(''.join(lst))