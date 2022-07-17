n = int(input())
for _ in range(n):
    word = input()
    cntr = 0
    cntl = 0
    check = 0
    for i in range(len(word)//2):
        if cntr == 0:
            if word[i] == word[-1-i]:
                continue
            else:
                cntl += 1
                cntr += 1
        if cntr == 1:
            if word[i] != word[-1-i-cntr]:
                cntr += 1
        if cntl == 1:
            if word[i+cntl] != word[-1-i]:
                cntl += 1
            

        if cntr == 2 and cntl == 2:
            break

    if min(cntr, cntl) == 0:
        print(0)
    elif min(cntr, cntl) == 1:
        print(1)
    else:
        print(2)
