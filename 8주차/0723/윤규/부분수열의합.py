from itertools import combinations

n = int(input())
arr = list(map(int, input().split(' ')))

comlst = set()
for i in range(1, n+1):
    c = list(combinations(arr, i))
    for j in range(len(c)):
        comlst.add(sum(c[j]))
# print(comlst)
for i in range(1, sum(arr)+2):
    if i not in comlst:
        print(i)
        break