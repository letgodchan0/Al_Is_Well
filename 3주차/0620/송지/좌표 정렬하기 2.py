case = int(input())
lst = [0 for i in range(case)]

for i in range(case):
    lst[i] = list(map(int, input().split()))
    
new_lst = sorted(lst, key = lambda x : (x[1], x[0]))

for i in range(len(new_lst)):
    print(new_lst[i][0], new_lst[i][1])