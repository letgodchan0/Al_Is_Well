n, m = map(int, input().split())
idong = [0] * 101
v = [0] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    idong[a] = b

ans = 0
now = [1]
    
while True:
    new = []
    
    for i in now:
        for j in range(1, 7):
            if i + j <= 100 and not v[i + j]:
                if not idong[i + j]:
                    v[i + j] = 1
                    new.append(i + j)
                else:
                    v[i + j] = 1
                    v[idong[i + j]] = 1
                    new.append(idong[i + j])
                    
    ans += 1
    now = new
           
    if v[100]:
        print(ans)
        break