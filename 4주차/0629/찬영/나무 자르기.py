n, m = map(int, input().split())
trees =[tree for tree in map(int, input().split())] 

start =  1
end = max(trees)

while start <= end :
    mid = (start+end)//2
    check = 0
    check = sum(map(lambda x : x - mid if x>mid else 0, trees))
    if check < m :
        end = mid - 1
    else:
        start = mid + 1

print(end)