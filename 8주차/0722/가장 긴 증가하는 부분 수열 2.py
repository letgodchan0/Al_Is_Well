def binary(num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if check[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start

n = int(input())
lst = list(map(int, input().split()))
check = [0]

for num in lst:
    if check[-1] < num:
        check.append(num)
    else:
        check[binary(num, 0, len(check)-1)] = num

print(len(check) - 1)
