n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst.extend(lst2)
lst.sort()

print(*lst)