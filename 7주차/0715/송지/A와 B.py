# def find(s):
#     global t, ans
#     s1 = s + 'A'
#     s2 = s[::-1] + 'B'

#     if ans:
#         return

#     if s1 not in t and s2 not in t:
#         return

#     if s1 == t or s2 == t:
#         ans = 1
#     else:
#         find(s1)
#         find(s2)


# s = input()
# t = input()
# ans = 0

# find(s)
# print(ans)


S = input()
T = input()

flag = False

while len(S) <= len(T):
    if S != T:
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1]
            T = T[::-1]
    else:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)