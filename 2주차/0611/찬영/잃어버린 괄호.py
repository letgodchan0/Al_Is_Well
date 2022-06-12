def plus(s):
    if '+' in s:
        tmp = s.split('+')
        s = sum(map(int, tmp))
    return int(s)

result = input().split('-')
result = list(map(plus, result))

ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]
print(ans)