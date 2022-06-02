def solution(s):
    result=[]
    answer=''
    answer_list=[]
    if len(s)==1:
        return 1
    for unit in range(1,(len(s)//2)+1):
        if unit==1:
            for j in range(1,len(s)+1,unit):
                result.append(s[j-unit:j])
#             print(result)    
            cnt=1
            j=1
            while cnt <= len(result):
                try:
                    if result[cnt-1]==result[cnt]:
                        cnt+=1
                        j+=1
                    else:
                        q_word=str(j)+result[cnt-1]
                        if q_word[0]=='1'and q_word[1].isalpha():
#                             print(q_word)
                            q_word=q_word.replace('1','')    
                        answer=answer+q_word
                        j=1
                        cnt+=1
                except:
                    q_word=str(j)+result[cnt-1]
                    if q_word[0]=='1'and q_word[1].isalpha():
#                         print(q_word)
                        q_word=q_word.replace('1','')   
                    answer=answer+q_word
                    j=1
                    cnt+=1
#             print(answer)
            answer_list.append(len(answer))
            answer=''
        else:
            result=[]
            for j in range(unit,len(s)+1000,unit):      # 여기서 1000을 더해준 이유가,, 특정 unit은 남은 글자를 포함 안시켜 줘서..
    #             print('unit:',unit,'//','j:',j)
                if s[j-unit:j]!='':
                    result.append(s[j-unit:j])
                if len(s[j-unit:j]) < unit:            # 다 확인했으면 더 이상 비교 안하도록 break
                    break
#             print(result)
            cnt=1
            j=1
            while cnt <= len(result):
                try:
                    if result[cnt-1]==result[cnt]:
                        cnt+=1
                        j+=1
                    else:
                        q_word=str(j)+result[cnt-1]
                        if q_word[0]=='1'and q_word[1].isalpha():
#                             print(q_word)
                            q_word=q_word.replace('1','')   
                        answer=answer+q_word
                        j=1
                        cnt+=1
                except:
                    q_word=str(j)+result[cnt-1]
                    if q_word[0]=='1' and q_word[1].isalpha():
#                         print(q_word)
                        q_word=q_word.replace('1','')     
                    answer=answer+q_word
                    j=1
                    cnt+=1
#             print(answer)
            answer_list.append(len(answer))
            answer=''
    return min(answer_list)