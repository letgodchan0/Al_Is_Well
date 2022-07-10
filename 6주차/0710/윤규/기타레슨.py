import sys
input = sys.stdin.readline
n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
answer = max(arr)


def divide(x):
    cnt = 1
    V = 0
    for i in range(len(arr)):
        if V + arr[i] > x:
            cnt += 1
            V = arr[i]
        else: V += arr[i]

        if cnt > m:
            break
    
    return cnt


start = max(arr)
end = sum(arr)
# check = 0
while start <= end:
    # if check == 0:
    mid = (start + end)//2
    cnt = divide(mid)
    if cnt > m:
        # check = 0
        start = mid + 1
    elif cnt <= m:
        # check = 0
        end = mid - 1
        answer = mid
    

print(answer)
