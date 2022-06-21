def find(lst, answer):
    global ans
    if len(lst) == 2 and answer > ans:
        ans = answer
        return

    for j in range(1, len(lst) - 1):
        find(lst[:j] + lst[j + 1:], answer + lst[j - 1] * lst[j + 1])


n = int(input())
lst = list(map(int, input().split()))
ans = 0

find(lst, 0)
print(ans)
