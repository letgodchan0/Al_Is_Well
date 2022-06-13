def solution(s):
    
    s = s.lstrip('{{')
    s = s.rstrip('}}')
    lst = s.split('},{')
    new_lst = [0] * len(lst)
    
    for i in range(len(lst)):
        new_lst[i] = lst[i].split(',')
    
    new_lst.sort(key = len)
    
    arr = [0] * 100001
    answer = []
    
    for lst in new_lst:
        for num in lst:
            if not arr[int(num)]:
                answer.append(int(num))
                arr[int(num)] = 1
                break
    
    return answer