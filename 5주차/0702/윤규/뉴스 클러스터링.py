def solution(str1, str2):
    answer = 0
    lst1 = []
    lst2 = []
    lst3 = []
    dic1 = dict()
    dic2 = dict()
    s1 = ''
    s2 = ''
    for i in range(len(str1)-1):
        for j in range(2):
            if 'a' <= str1[i + j] <= 'z' or 'A' <= str1[i + j] <= 'Z':
                s1 += str1[i + j]
            else:
                s1 = ''
                break
            if len(s1) == 2:
                s1 = s1.lower()
                lst1.append(s1)
                if dic1.get(s1):
                    dic1[s1] += 1
                else:
                    dic1[s1] = 1
                s1 = ''
    for i in range(len(str2)-1):
        for j in range(2):
            if 'a' <= str2[i + j] <= 'z' or 'A' <= str2[i + j] <= 'Z':
                s2 += str2[i + j]           
            else:
                s2 = ''
                break
            if len(s2) == 2:
                s2 = s2.lower()
                lst2.append(s2)
                if s2 in dic1 and dic1[s2]>0:
                    lst3.append(s2)
                    dic1[s2] -= 1
                s2 = ''
    
    print(lst1, lst2, lst3)
    answer = 1 if len(lst1) == 0 and len(lst2) == 0 else len(lst3) / (len(lst1) + len(lst2) - len(lst3))
    answer = int(answer * 65536)
    return answer





str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))