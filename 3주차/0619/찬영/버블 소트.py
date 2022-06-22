def split(lst, n):
    if n == 1:
        return lst
    left = lst[:n // 2]
    right = lst[n // 2:]
    left = split(left, len(left))
    right = split(right, len(right))
    return merge(left, right)

def merge(left, right):
    global cnt
    check = []
    i = j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                check.append(left[i])
                i += 1
            else:
                check.append(right[j])
                j += 1
                cnt += len(left) - i

        elif len(left) > i:
            check.append(left[i])
            i += 1
        elif len(right) > j:
            check.append(right[j])
            j += 1
    return check

n = int(input())
lst = list(map(int, input().split()))
cnt = 0
split(lst, n)
print(cnt)