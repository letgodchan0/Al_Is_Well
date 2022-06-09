"""
제일 큰 사분면으로 나눠서 생각한다.
사분면으로 나눠서, 다시 쪼갠다 (쪼갤 때, 좌표 초기화)

"""
N, r, c = map(int, input().split())
result = 0

while N:
    plus = (2 ** (N - 1)) ** 2

    if r < 2 ** (N - 1) and c < 2 ** (N - 1):
        pass


    elif r < 2 ** (N - 1) and c >= 2 ** (N - 1):
        result += plus
        c -= 2 ** (N - 1)


    elif r >= 2 ** (N - 1) and c < 2 ** (N - 1):
        result += plus * 2
        r -= 2 ** (N - 1)


    elif r >= 2 ** (N - 1) and c >= 2 ** (N - 1):
        result += plus * 3
        r -= 2 ** (N - 1)
        c -= 2 ** (N - 1)
    
    N -= 1

print(result)