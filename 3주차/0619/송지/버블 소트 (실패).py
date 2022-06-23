swap = 0
n = int(input())
lst = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            swap += 1

print(swap)

# 아니 이거 어케 해요 ;;;;;;;;;;;;;
