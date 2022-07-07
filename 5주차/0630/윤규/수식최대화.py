from itertools import permutations
from copy import deepcopy

def calculate(numbers, order):
    numbers = deepcopy(numbers)
    for o in order:
        new_number = []
        i = 0
        while i < len(numbers):
            if numbers[i] == o:
                if o == '+':
                    if new_number:
                        new_number[-1] = (new_number[-1] + numbers[i+1])
                        i += 1
                    else:
                        new_number.append(numbers[i-1] + numbers[i+1])
                        i += 1
                elif o == '*':
                    if new_number:
                        new_number[-1] = (new_number[-1] * numbers[i+1])
                        i += 1
                    else:
                        new_number.append(numbers[i-1] + numbers[i+1])
                        i += 1
                elif o == '-':
                    if new_number:
                        new_number[-1] = (new_number[-1] - numbers[i+1])
                        i += 1
                    else:
                        new_number.append(numbers[i-1] + numbers[i+1])
                        i += 1
            else: 
                new_number.append(numbers[i])
            i += 1
        numbers = new_number[:]
    return new_number[0]

def solution(expression):
    numbers = []
    cal = set()
    ss = ''
    for s in expression:
        if s == '-' or s == '+'  or s == '*' :
            numbers.append(int(ss))
            numbers.append(s)
            cal.add(s)
            ss = ''
        else:
            ss += s
    numbers.append(int(ss))
    
    orders = list(permutations(cal, len(cal)))
    
    maxV = 0
    for order in orders:
        if maxV < abs(calculate(numbers, order)):
            maxV = abs(calculate(numbers, order))
    

    return maxV

print(solution("50*6-3*2"))