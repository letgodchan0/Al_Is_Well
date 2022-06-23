# #버블 소트로 풀면 시간 초과...ㅠ
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# swap = 0

# if n == 1:
#     pass
# else:
#     for m in range(n,0,-1):
#         for i in range(m-1):
#             if arr[i] > arr [i+1]:
#                 swap += 1
#                 arr[i], arr [i+1] = arr[i+1], arr [i]
# print(swap)

#병합정렬
#우측 배열의 값이 insert 되는 경우에 좌측 배열에 자신보다 큰 수의 개수가 swap 횟수
#좌측 배열에서 insert 되는 경우에는 swap이 일어나지 않는다

import sys

def merge_sort(start, end):
    global swap, arr

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                temp.append(arr[a])
                a += 1
            else:
                temp.append(arr[b])
                b += 1
                swap += (mid - a + 1)

        if a <= mid:
            temp = temp + arr[a:mid + 1]
        if b <= end:
            temp = temp + arr[b:end + 1]

        for i in range(len(temp)):
            arr[start + i] = temp[i]

n = int(sys.stdin.readline())
swap = 0
arr = list(map(int, sys.stdin.readline().split()))
merge_sort(0, n - 1)
print(swap)