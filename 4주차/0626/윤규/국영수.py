n = int(input())
slst = []
for i in range(n):
    name, ks, es, ms = input().split(' ')
    slst.append((name, int(ks), int(es), int(ms)))


slst.sort(key=lambda x: (-x[1], x[2] , -x[3], x[0]))
for name in slst:
    print(name[0])