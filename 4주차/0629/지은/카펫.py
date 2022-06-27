def solution(brown, yellow):
    
    for m in range(1,int(yellow**0.5)+1):
        if yellow % m != 0:
            continue
        else:
            n = yellow // m
            if brown == 2*n + 2*m + 4:
                break

    return [n+2, m+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))