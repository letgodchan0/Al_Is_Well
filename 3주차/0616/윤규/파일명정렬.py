def solution(files):
    answer = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    for file in files:
        
        check = 0
        head = ''
        number = ''
        for letter in file:
            if letter not in numbers:
                if check == 0:
                    head += letter
                elif check == 1 :
                    break
                
            elif letter in numbers:
                if check == 0 or check == 1:
                    number += letter
                    check = 1
                    if len(number) == 5:
                        break
                
                

        word = [file, head.upper(), int(number.lstrip('0')) if number.lstrip('0') else 0]
        answer.append(word)
    
    answer.sort(key=lambda x: (x[1], x[2]))
    
    ans = []
    for i in range(len(answer)):
        ans.append(answer[i][0])

    return ans


print(bool('00001'.lstrip('0')))
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))