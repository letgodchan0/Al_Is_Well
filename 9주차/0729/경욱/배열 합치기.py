_ = input()
a = list(map(int, input().split()))
a += list(map(int, input().split()))
print(*sorted(a))