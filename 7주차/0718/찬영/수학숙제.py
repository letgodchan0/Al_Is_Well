def check(word):
    lst = []
    i = 0
    while i < len(word):
        if word[i].isdigit():
            tmp = ''
            while i < len(word):
                if word[i].isdigit():
                    tmp += word[i]
                    if i == len(word) - 1:
                        lst.append(int(tmp))
                        break
                    i += 1
                else:
                    lst.append(int(tmp))
                    break
        i += 1
    return lst
n = int(input())
result = []
for _ in range(n):
    word = input()
    number = check(word)
    if number:
        result.extend(number)
result.sort()
for res in result:
    print(res)