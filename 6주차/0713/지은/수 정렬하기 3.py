#.sort(), sorted() -> 메모리 초과
#heapq 사용 -> 메모리 초과
import sys

n = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(n):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)