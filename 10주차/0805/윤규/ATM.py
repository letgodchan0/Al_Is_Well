n = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()
ans = 0
for i in range(1, n+1):
    ans += sum(arr[0:i])
print(ans)