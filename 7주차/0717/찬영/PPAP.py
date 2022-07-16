word = input()
stack = ['x'] * 3
for i in range(len(word)):
    if word[i] == 'P':
        if stack[-1] == 'A' and stack[-2] == 'P' and stack[-3] == 'P':
            stack.pop(-1)
            stack.pop(-1)
            stack.pop(-1)
    stack.append(word[i])

if ''.join(stack[3:]) == 'P':
    print('PPAP')
else:
    print('NP')