def palindrome(word):
    return True if word == word[::-1] else False

def pseudo1(word):
    cnt = 0
    start = 0; end = len(word) - 1
    check = True
    if palindrome(word[1:]):
        return True

    while start < end:
        if word[start] == word[end]:
            start +=1; end -=1
        else:
            end -=1
            cnt +=1

        if cnt > 1:
            check = False
            break

    return True if check else False

def pseudo2(word):
    cnt = 0
    start = 0; end = len(word) - 1
    check = True
    if palindrome(word[1:]):
        return True

    while start < end:
        if word[start] == word[end]:
            start +=1; end -=1
        else:
            start += 1
            cnt +=1

        if cnt > 1:
            check = False
            break

    return True if check else False

t = int(input())
for _ in range(t):
    word = input()
    answer = 2
    if palindrome(word):
        answer = 0
    elif pseudo1(word) or pseudo2(word):
        answer = 1
    print(answer)


