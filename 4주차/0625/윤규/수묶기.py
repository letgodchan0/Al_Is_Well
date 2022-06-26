

n = int(input())
numbers = list(int(input()) for _ in range(n))

minus = []
plus = []
o = 0

for number in numbers:
    if number <= 0:
        minus.append(number)
    elif number == 1:
        o += 1
    else:
        plus.append(number)

plus.sort(reverse=True)
minus.sort()
sum = 0
# 홀수 개일 때
if len(plus) % 2:
    for i in range(0, len(plus)-1, 2):
        sum += plus[i] * plus[i+1]
    sum += plus[-1]
else:
    for i in range(0, len(plus), 2):
        sum += plus[i] * plus[i+1]

if len(minus) % 2:
    for i in range(0, len(minus)-1, 2):
        sum += minus[i] * minus[i+1]
    sum += minus[-1]
else:
    for i in range(0, len(minus), 2):
        sum += minus[i] * minus[i+1]
sum += o
print(sum)
