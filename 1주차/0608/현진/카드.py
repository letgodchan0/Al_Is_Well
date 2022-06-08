# 카드
import sys
input = sys.stdin.readline

N = int(input())
arr = {}

for _ in range(N):
    card = int(input())
    if card in arr:
        arr[card] += 1
    else:
        arr[card] = 1

result = sorted(arr.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])