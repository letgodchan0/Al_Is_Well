import sys
input = sys.stdin.readline

def dfs(depth, total, plus, minus, multiply, divide):
    global maxNum, minNum
    if depth == N:
        maxNum = max(total, maxNum)
        minNum = min(total, minNum)
        return
    
    if plus:
        dfs(depth + 1, total + number[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - number[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * number[depth], plus, minus, multiply -1, divide)
    if divide:
        dfs(depth + 1, int(total / number[depth]), plus, minus, multiply, divide - 1)

N = int(input())
number = list(map(int, input().split()))
operation = list(map(int, input().split()))

maxNum = -1e9
minNum = 1e9

dfs(1, number[0], operation[0], operation[1], operation[2], operation[3])
print(maxNum)
print(minNum)