a = int(input())
lst = [list(map(int, input().split())) for _ in range(a)]

lst.sort()
lst = sorted(lst, key=lambda x:x[1])
ans = 1
x = lst[0][1]

for con in range(1, a):
    if x <= lst[con][0]:
        x = lst[con][1]
        ans += 1
        
print(ans)