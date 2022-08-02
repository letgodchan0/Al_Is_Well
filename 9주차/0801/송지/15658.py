def find(idx, ans, a, b, c, d):
    global max_ans, min_ans, lst
    
    if idx > len(lst) - 1:
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
        return

    if a > 0:
        find(idx + 1, ans + lst[idx], a - 1, b, c, d)
    if b > 0:
        find(idx + 1, ans - lst[idx], a, b - 1, c, d)
    if c > 0:
        find(idx + 1, ans * lst[idx], a, b, c - 1, d)
    if d > 0:
        find(idx + 1, ans // lst[idx] if ans > 0 else -((-ans) // lst[idx]), a, b, c, d - 1)
        

n = int(input())
max_ans = -9999999999
min_ans = 9999999999

lst = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

find(1, lst[0], a, b, c, d)
print(max_ans)
print(min_ans)