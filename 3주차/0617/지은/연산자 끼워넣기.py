import sys

def dfs(depths, tot, operators):
    if depths == n:
        results.append(tot)
        return 
    if operators[0]:
        dfs(depths+1, tot+nums[depths], [operators[0]-1,operators[1],operators[2],operators[3]])
    if operators[1]:
        dfs(depths+1, tot-nums[depths], [operators[0],operators[1]-1,operators[2],operators[3]])
    if operators[2]:
        dfs(depths+1, tot*nums[depths], [operators[0],operators[1],operators[2]-1,operators[3]])
    if operators[3]:
        dfs(depths+1, int(tot/nums[depths]), [operators[0],operators[1],operators[2],operators[3]-1])
    
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
results = []

dfs(1, nums[0], operators)

print(max(results))
print(min(results))