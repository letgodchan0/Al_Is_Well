n, m, k = map(int,input().split())
#1부터 N까지의 수를 한 번씩 이용해서 
#가장 긴 증가하는 부분 수열(LIS)의 길이가 M이고, 
#가장 긴 감소하는 부분 수열(LDS)의 길이가 K
#A = {10, 20, 10, 30, 20, 50}인 경우 LIS 길이 4 LDS 길이 3
if m + k -1 > n or m * k < n:
    #조건2) 감소 수열을 증가수열의 갯수만큼 나열
    print(-1)
else:
    l = list(range(k, 0, -1))
    n -= k  #n개 중 k개 숫자 사용
    m -= 1  
    while m:
        l.extend(range(k+n//m,k,-1))
        k += n//m
        n -= n//m
        m -= 1
    print(*l)