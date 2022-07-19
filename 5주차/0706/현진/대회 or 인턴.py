n, m, k = map(int, input().split())
ans = 0

# 2명, 1명 팀을 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일 때
while n >= 2 and m >= 1 and n + m >= k + 3:
    n -= 2
    m -= 1
    ans += 1
print(ans)