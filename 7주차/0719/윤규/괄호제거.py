from itertools import combinations

exp = input()
bracketlst = []
llst = []

for i in range(len(exp)):
    if exp[i] == '(':
        llst.append(i)
    if exp[i] == ')':
        bracketlst.append([llst.pop(), i])
                


newlst = set()
newexp = ''
for i in range(1, len(bracketlst)+1):
    blst = list(combinations(bracketlst, i))
    for b in blst:
        lst = []
        for k in range(i):
            lst.extend(b[k])
        for j in range(len(exp)):
            if j not in lst:
                newexp += exp[j]
        newlst.add(newexp)
        newexp = ''

newlst = list(newlst)
newlst.sort()
for i in range(len(newlst)):
    print(newlst[i])
