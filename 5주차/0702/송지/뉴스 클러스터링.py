def solution(str1,str2):
    
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
    
    inter = sum([min(str1.count(word), str2.count(word)) for word in intersection])
    uni = sum([max(str1.count(word),str2.count(word)) for word in union])

    if uni ==0:
        return 65536
    return int(inter/uni * 65536)