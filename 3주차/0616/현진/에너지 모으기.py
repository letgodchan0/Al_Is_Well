def find(s):
    global maxV

    if (len(arr) == 2):
        if (s > maxV):
            maxV = s
        return 
    else:
        for i in range(1, len(arr) - 1):
            r = arr[i - 1] * arr[i + 1]
            tmp = arr[i]
            del arr[i]
            find(s + r)
            arr.insert(i, tmp)

n = int(input())
arr = list(map(int, input().split()))
maxV = 0
find(0)
print(maxV)