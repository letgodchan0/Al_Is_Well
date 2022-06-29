# Back_1744
import sys
input = sys.stdin.readline

N = int(input())
plus = [] # 양수 리스트
minus = [] # 음수 리스트
maxV = 0

for _ in range(N):
    n = int(input())
    if n > 1:
        plus.append(n)
    elif n == 1:
        maxV += 1   # 1이면 바로 더하기
    else:
        minus.append(n)

plus.sort(reverse=True) # 양수는 큰 수부터 정렬
minus.sort()    # 음수는 작은 수부터 정렬

# 양수 리스트 더해주기
# 양수가 짝수개이면, 두개씩 곱해준다
if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        maxV += plus[i] * plus[i + 1]
else:
    for i in range(0, len(plus) - 1, 2):
        maxV += plus[i] * plus[i + 1]
    maxV += plus[len(plus) - 1]

# 음수 리스트 더해주기
# 음수가 짝수개이면 두개씩 곱해준다.
if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        maxV += minus[i] * minus[i + 1]
else:
    for i in range(0, len(minus) - 1, 2):
        maxV += minus[i] * minus[i + 1]
    maxV += minus[len(minus) - 1]

print(maxV)