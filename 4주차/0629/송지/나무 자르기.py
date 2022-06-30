import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
end = max(lst)
start = 0

while True:
    
    find = int((end + start) / 2)
    answer = 0
    
    for i in lst:
        if i > find:
            answer += i - find
            
    if answer > m:
        start = find
    elif answer < m:
        end = find
    else:
        print(find)
        break
    
    if (end - start) <= 1:
        print(start)
        break