def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    id_lst = []
    check = 0
    
    for i in range(len(new_id)):
        if '0'<=new_id[i]<='9' or 'a' <= new_id[i] <= 'z' or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            answer += new_id[i]
    for i in range(len(answer)):
        if answer[i] == '.' and check == 0:
            id_lst.append(answer[i])
            check = 1
        elif answer[i] != '.':
            id_lst.append(answer[i])
            check = 0
    if id_lst and id_lst[0] == '.':
        id_lst.pop(0)
    if id_lst and id_lst[-1] == '.':
        id_lst.pop()
    if not id_lst:
        id_lst.append('a')
    if len(id_lst) >= 16:
        id_lst = id_lst[:15]
    if id_lst[-1] == '.':
        id_lst.pop()
    if len(id_lst) <= 2:
        while len(id_lst) != 3:
            id_lst += id_lst[-1]
    answer = ''
    for id in id_lst:
        answer += id


    return answer


new_id=	"...!@BaT#*..Y.abcdefghijklm"
print(solution(new_id))