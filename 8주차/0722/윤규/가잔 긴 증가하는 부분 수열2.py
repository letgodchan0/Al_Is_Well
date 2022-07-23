a = int(input())
arr = list(map(int, input().split(' ')))

lst = [0]
arr = [0] + arr
for a in arr:
    if lst[-1] < a:
        lst.append(a)
    elif lst[-1] > a:
        start = 1
        end = len(lst)-1
        check = 0
        while start < end:
            mid = (start + end) // 2
            if lst[mid] < a:
                start = mid + 1
            elif lst[mid] > a:
                end = mid 
            else:
                check = 1
                break
        
        if check == 0:
            lst[end] = a

print(len(lst)-1)
