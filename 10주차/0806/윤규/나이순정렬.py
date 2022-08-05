

n = int(input())
name = []
for i in range(n):
    a, b = input().split(' ')
    a = int(a)
    name.append([a, b])
name.sort(key=lambda x : x[0])
for i in range(n):
    print(*name[i])