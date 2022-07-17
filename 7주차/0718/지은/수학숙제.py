import re

n = int(input())
result = []
for _ in range(n):
    word = input()
    nums = re.split('[a-z]', word)
    while '' in nums:
        nums.remove('')
    result.extend(nums)
result = list(map(int,result))
result.sort()
print(*result, sep='\n')