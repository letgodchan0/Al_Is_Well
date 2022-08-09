a = int(input())
a_lst = list(map(int, input().split()))
b = int(input())
b_lst = list(map(int, input().split()))
dict = {}

for num in a_lst:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

for num in b_lst:
    try:
        print(dict[num], end = ' ')
    except:
        print(0, end = ' ')