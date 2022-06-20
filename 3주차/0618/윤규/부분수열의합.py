n, s = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

cnt = 0

def search(i, s, want, check):
    global cnt
    if i == n:
        if check == 1 and s == want:
            cnt += 1
        return
    
    else:
        search(i+1, s+ arr[i], want, 1)
        search(i+1, s, want, 1 if check==1 else 0)
    
search(0, 0, s, 0)
print(cnt)