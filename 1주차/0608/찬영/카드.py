import sys
n = int(input())
check = {}
for _ in range(n):
    number = int(sys.stdin.readline())
    check[number] = check.get(number, 0) + 1

lst = sorted(check.keys(), key = lambda x: (-check[x], x ))
print(lst[0])