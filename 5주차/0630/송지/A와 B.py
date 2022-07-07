def find(s):
    global t, ans
    s1 = s + 'A'
    s2 = s[::-1] + 'B'

    if ans:
        return

    if s1 not in t and s2 not in t:
        return

    if s1 == t or s2 == t:
        ans = 1
    else:
        find(s1)
        find(s2)


s = input()
t = input()
ans = 0

find(s)
print(ans)