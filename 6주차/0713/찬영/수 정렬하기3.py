import sys
n = int(input())
numbers = {}
for _ in range(n):
    number = int(sys.stdin.readline())
    numbers[number] = numbers.get(number, 0) + 1
for i in sorted(numbers.keys()):
    for _ in range(numbers[i]):
        print(i)

# 카운팅 정렬, but 메모리 초과
count = [0] * (max(numbers.values)+1)
tmp = [0] * len(numbers.values)
for i in numbers.values:
    count[i] += 1
for i in range(1,len(count)):
    count[i] += count[i-1]

for number in range(len(numbers)-1, -1, -1):
    tmp[count[numbers[number]]-1] = numbers[number]
    count[numbers[number]] -= 1
for i in tmp:
    print(i)