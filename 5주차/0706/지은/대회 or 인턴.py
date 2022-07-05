n, m, k = map(int,input().split())
team = min(n//2, m)

while k > n+m - 3*team:
    team -= 1

print(team)