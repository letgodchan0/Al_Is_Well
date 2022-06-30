import re
def solution(name):
    score={'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    change=0
    for i in name:
        change+=score[i]

    startA = re.compile('[A]+')
    check = re.findall(startA, name[1:])  # 연속된 A를 담아줌
    cnt1=0
    if check:
        tmp = name[1:].split(max(check))
        if '' in tmp:
            cnt1=len(max(check))
        else:
            cnt2 = 2*len(tmp[0])+len(tmp[-1])
            cnt1=min(len(name)-1, cnt2)
            return change + cnt1
    
    # 알파벳 바꾸는데 키 + 오른쪽으로 쭉 가는 경우 - A가 연속되어 있다면 그냥 건너뛰는 경우
    return change+len(name)-1