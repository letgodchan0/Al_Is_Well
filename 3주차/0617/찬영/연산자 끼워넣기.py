from itertools import combinations, permutations

def Max(lst):
    global max_value
    start = number[0]
    for i in range(len(lst)):

        if lst[i] == '+':
            start += number[i+1]
        elif lst[i] == '-':
            start -= number[i+1]
        elif lst[i] == '*':
            start *= number[i+1]
        elif lst[i] == '/':
            if start < 0:
                start = -((start * -1) // number[i+1])
            else:
                start //= number[i+1]

    max_value = start if start > max_value else max_value

def Min(lst):
    global min_value
    start = number[0]
    for i in range(len(lst)):

        if lst[i] == '+':
            start += number[i+1]
        elif lst[i] == '-':
            start -= number[i+1]
        elif lst[i] == '*':
            start *= number[i+1]
        elif lst[i] == '/':
            if start < 0:
                start = -((start * -1) // number[i+1])
            else:
                start //= number[i+1]

    min_value = start if start < min_value else min_value
    return


n = int(input())
number = list(map(int, input().split()))
check = list(map(int, input().split()))
lsts = []
for i in range(4):
    if i == 0 and check[i]:
        lsts.extend(['+'] * check[i])
    elif i == 1 and check[i]:
        lsts.extend(['-'] * check[i])
    elif i == 2 and check[i]:
        lsts.extend(['*'] * check[i])
    elif i == 3 and check[i]:
        lsts.extend(['/'] * check[i])

lsts = list(set(permutations(lsts, n-1)))
lsts = list(map(lambda x : list(x), lsts))
max_value = -100000000
min_value = 100000000
for lst in lsts:
    Max(lst); Min(lst);
print(max_value)
print(min_value)
