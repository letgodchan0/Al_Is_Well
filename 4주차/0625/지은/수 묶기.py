n = int(input())
minus = []
plus = []
one = []

for idx in range(n):
    tmp = int(input())
    if tmp > 1:
        plus.append(tmp)
    elif tmp==1:
        one.append(tmp)
    else:
        minus.append(tmp)

plus.sort(reverse=True)
minus.sort()
answer = 0

if len(plus)%2==0:
    for i in range(0,len(plus),2):
        answer += plus[i] * plus[i+1]
else:
    for i in range(0,len(plus)-1,2):
        answer += plus[i] * plus[i+1]
    answer += plus[-1]

if len(minus)%2==0: #홀수가 짝수개 있을 때
    for i in range(0,len(minus),2):
        answer += minus[i] * minus[i+1]
else:
    for i in range(0,len(minus)-1,2):
        answer += minus[i] * minus[i+1]
    answer += minus[-1]

answer += len(one)

print(answer)