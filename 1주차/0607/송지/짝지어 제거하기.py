def solution(s):
    
    lst = list(s)

    while lst:
        
        new_lst = ['기본값']

        for word in lst:
            if new_lst[-1] != word:
                new_lst.append(word)
            else:
                new_lst.pop()
                
        if new_lst[1:] == lst:
            return 0

        lst = new_lst[1:]
        
    return 1