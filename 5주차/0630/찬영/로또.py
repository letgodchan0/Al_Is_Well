from itertools import combinations
import sys
while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if len(numbers) == 1:
        break

    numbers = sorted(numbers[1:])

    for number in combinations(numbers, 6):
        print(*number)
    print()