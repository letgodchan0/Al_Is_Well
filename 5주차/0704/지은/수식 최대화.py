from itertools import permutations

def operation(num1, num2, op):  #수식과 연산자를 받아 연산 수행
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    array=[]
    tmp=""
    for i in exp:   #숫자와 연산자 분리
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack
            
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))  #연산순서 리스트
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))