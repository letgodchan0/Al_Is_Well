def solution(s):
    answer = []
    elements = {}
    lst = s.split(',')
    for l in lst:
        l = l.strip('{')
        l = l.strip('}')
        l = int(l)
        #{, }를 strip
        elements[l] = elements.get(l,0) + 1
    
    elements_s = sorted(elements.items(), key = lambda x:x[1], reverse=True)
    #원소들의 개수 순으로 나열

    for el in elements_s:
        answer.append(el[0])

    return answer
