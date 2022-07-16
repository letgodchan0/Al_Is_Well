from itertools import combinations

words = input()
stack = []
idx = []
result=[]
for i in range(len(words)):
    if words[i] == '(':
        stack.append(i)
    elif words[i] == ')':
        idx.append([stack.pop(), i])

for i in range(1, len(idx)+1):
    combs = list(combinations(idx, i))
    for comb in combs:
        check = []
        answer = []
        for com in comb:
            check.append(com[0]); check.append(com[1])

        for j in range(len(words)):
            if j in check:
                continue
            else:
                answer.append(words[j])
        result.append(''.join(answer))
result = set(result)
result = sorted(list(result))
for res in result:
    print(res)
