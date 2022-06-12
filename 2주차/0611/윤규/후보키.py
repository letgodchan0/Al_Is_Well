

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    cand = []
    def combi(n, r, s, comb, A, cand):
        if r == 0:
            cand.append(comb[:])                    # 같은 주소 참조 하니깐 조심    
        else:
            for i in range(s, n-r+1):
                comb[r-1] = A[i]
                combi(n, r-1, i+1, comb, A, cand)
                

    # col 개수 만큼 조합 구하기
    for i in range(1, col + 1):
        comb = [0] * i
        A = [j for j in range(col)]     
        combi(col, i, 0, comb, A, cand)
        
        
        
    # 유일한 것 찾기
    uniq = []
    for can in cand:
        tmp = [tuple([item[i] for i in can]) for item in relation]
        if len(set(tmp)) == row:
            uniq.append(tuple(can))

    
    ans = set(uniq)
    for i in range(len(uniq)):
        for j in range(i+1, len(uniq)):
            if len(uniq[i]) == len(set(uniq[i]) & set(uniq[j])):
                ans.discard(uniq[j])      
    return len(ans)
# a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# print(solution(a))