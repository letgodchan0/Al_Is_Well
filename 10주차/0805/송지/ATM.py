a = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
answer = 0

for i in range(len(lst)):
    answer += lst[i] * (i + 1)
    
print(answer)