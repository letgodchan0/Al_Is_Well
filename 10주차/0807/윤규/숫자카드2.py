n = int(input())
numlst = list(map(int, input().split(' ')))
lst = [0] * 10000001
minuslst = [0] * 10000001
for i in range(n):
    if numlst[i] >= 0:
        lst[numlst[i]] += 1
    else:
        minuslst[numlst[i]*-1] += 1

m = int(input())
numl = list(map(int, input().split(' ')))
ans = [0] * m

for i in range(m):
    if numl[i] >= 0:
        ans[i] = lst[numl[i]]
    else:
        ans[i] = minuslst[numl[i]*-1]

print(*ans)

