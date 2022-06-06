import sys
input = sys.stdin.readline

new_dict = {}

for i in range(int(input())):
    a = int(input())
    if a in new_dict:
        new_dict[a] += 1
    else:
        new_dict[a] = 1

max = 0
max_key = 'what'

for key in new_dict:
    if new_dict[key] > max:
        max = new_dict[key]
        max_key = key
    elif new_dict[key] == max:
        if key < max_key:
            max_key = key
        
print(max_key)