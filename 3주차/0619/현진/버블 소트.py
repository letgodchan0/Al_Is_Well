# merge_sort방식
import sys
input = sys.stdin.readline

def merge(x, y):
    global cnt
    len_x, len_y = len(x), len(y)
    i, j = 0, 0
    temp = []

    while i < len_x and j < len_y:
        if x[i] > y[j]:
            temp.append(y[j])
            j += 1
            cnt += len_x - i
        else:
            temp.append(x[i])
            i += 1
    if i == len_x:
        temp.extend(y[j:])
    else:
        temp.extend(x[i:])
    return temp

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    return merge(merge_sort(arr[left:mid + 1]), merge_sort(arr[mid + 1:]))
N = int(input())
cnt = 0
arr = list(map(int, input().split()))
merge_sort(arr)
print(cnt)
