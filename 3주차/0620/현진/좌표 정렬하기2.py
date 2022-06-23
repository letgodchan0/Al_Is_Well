N = int(input())
map = []

for _ in range(N):
    x, y = map(int, input().split())
    map.append((x, y))

arr = sorted(map, key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])