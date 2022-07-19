from itertools import combinations

expression = list(input()) 
bs, bi = [],[]      # 괄호쌍 찾을 스택, 괄호쌍 인덱스 저장
result = set()      # 중복 없는 결과

for i, ex in enumerate(expression): # 괄호쌍 인덱스 저장 및 expression에서 괄호 제거
    if ex == '(':
        expression[i]=''
        bs.append(i)
    if ex == ')':
        expression[i] = ''
        bi.append([bs.pop(), i])    

for i in range(len(bi)):        # 괄호쌍의 조합을 이용해 괄호 추가
    for j in combinations(bi, i):
        B = expression[:]
        for s,e in j:           # 괄호쌍 채우기
            B[s] = '('
            B[e] = ')'   
        result.add(''.join(B))

print(*sorted(result), sep='\n')