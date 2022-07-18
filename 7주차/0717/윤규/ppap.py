# 시간초과
# word = input()


# def ppap(word):
#     if word == 'PPAP':
#         return 'PPAP'
#     else:
#         for i in range(len(word)):
#             if word[i] == 'A':
#                 try:
#                     if word[i-2] == 'P' and word[i-1] == 'P' and word[i+1] == 'P':
#                         word = word.replace('PPAP', 'P')
#                         return ppap(word)
#                     else:
#                         return 'NP'
#                 except:
#                     return 'NP'
#         else:
#             return 'NP'

# print(ppap(word))

word = list(input())
cntP = 0
check = 0
try:
    for i in range(len(word)):
        if word[i] == 'P':
            cntP += 1
        # A라면
        else:
            # 연속 A라면
            if word[i+1] == 'A':
                print("NP")
                check = 1
                break
            # AP라면
            elif word[i+1] == 'P':
                if cntP < 2:
                    print("NP")
                    check = 1
                    break
                elif cntP >= 2:
                    cntP -= 2
                    continue
    
    if check == 0 and cntP == 1:
        print("PPAP")
    elif check == 0 and cntP > 1:
        print("NP")
except:
    print("NP")

