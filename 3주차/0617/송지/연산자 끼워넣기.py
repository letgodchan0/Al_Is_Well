import itertools

n = int(input())
lst = list(map(int, input().split()))
giho = list(map(int, input().split()))
use = []

use += ['+'] * giho[0]
use += ['-'] * giho[1]
use += ['*'] * giho[2]
use += ['/'] * giho[3]

use = list(set(itertools.permutations(use, len(use))))
min_num = 1000000000
max_num = -1000000000

for u in use:
    ans = lst[0]
    for i in range(n - 1):
        if u[i] == '+':
            ans += lst[i + 1]
        elif u[i] == '-':
            ans -= lst[i + 1]
        elif u[i] == '*':
            ans *= lst[i + 1]
        else:
            if ans >= 0:
                ans //= lst[i + 1]
            else:
                ans = -(-ans // lst[i + 1])

    if min_num > ans:
        min_num = ans
    if max_num < ans:
        max_num = ans

print(max_num)
print(min_num)
