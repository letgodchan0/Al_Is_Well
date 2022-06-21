import sys
input = sys.stdin.readline

case = int(input())
lst = [0 for i in range(case)]
for i in range(case):
    lst[i] = int(input())

lst.sort()
    
for i in range(case):
    print(lst[i])