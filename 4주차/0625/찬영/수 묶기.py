import sys
n = int(input())
pos = []
neg = []
for _ in range(n):
    number = int(sys.stdin.readline())
    if number > 0 :
        pos.append(number)
    else:
        neg.append(number)
pos.sort(reverse=True); neg.sort()
pos_num = neg_num = 0

if not len(pos) % 2:
    for i in range(len(pos)//2):
        if pos[2*i] > 1 and pos[2*i+1] > 1:
            pos_num += pos[2*i] * pos[2*i+1]
        else:
            pos_num += sum(pos[i*2:])
            break
else:
    for i in range(len(pos) // 2):
        if pos[2 * i] > 1 and pos[2 * i + 1] > 1:
            pos_num += pos[2 * i] * pos[2 * i + 1]
        else:
            pos_num += sum(pos[i*2:-1])
            break
    pos_num += pos[-1]


if not len(neg) % 2:
    for i in range(len(neg)//2):
        neg_num += neg[2*i] * neg[2*i+1]
else:
    for i in range(len(neg)//2):
        neg_num += neg[2*i] * neg[2*i+1]
    neg_num += neg[-1]

print(pos_num+neg_num)