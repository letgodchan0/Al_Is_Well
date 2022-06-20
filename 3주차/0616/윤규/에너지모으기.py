n = int(input())
arr = list(map(int, input().split()))

def energy(arr, e):
    global ans
    if len(arr) == 2:
        if e > ans:
            ans = e
        return
    else:
        for i in range(1, len(arr)-1):
            e2 = arr[i-1]*arr[i+1]
            arr2 = arr[:] 
            arr2.pop(i)
            energy(arr2, e+e2)

ans = 0
energy(arr, 0)
print(ans)