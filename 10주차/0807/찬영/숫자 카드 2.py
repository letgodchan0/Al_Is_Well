from collections import Counter
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

count = Counter(cards)
answer = [count[number] if number in count else 0 for number in numbers]
print(*answer)