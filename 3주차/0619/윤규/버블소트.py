n = int(input())
arr = list(map(int, input().split()))


def mergeSort(start, end):
    global cnt
    if start < end:
        mid = (start + end)//2
        mergeSort(start, mid)
        mergeSort(mid+1, end)

        a = start
        b = mid + 1
        # 가운데 기점으로 a는 왼쪽, b는 오른쪽, 하나라도 넘어가면 중단
        new = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                new.append(arr[a])
                a += 1
            else:
                new.append(arr[b])
                b += 1
                cnt += (mid-a)+1
        
        if a <= mid:
            new = new + arr[a:mid+1]
        if b <= mid:
            new = new + arr[b:end+1]

        # arr[start: end+1] = new

        # 이거는 시간 안에 되고 위에 거는 시간초과 나는 이유
        for i in range(len(new)):
            arr[start+i] = new[i]



cnt = 0
mergeSort(0,n-1)
print(cnt)