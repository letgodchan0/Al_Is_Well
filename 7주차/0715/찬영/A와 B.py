def A(word):
    return word[:-1]

def B(word):
    word = word[:-1]
    return word[::-1]

s = input(); t = input()
while len(s) != len(t): t = A(t) if t[-1] == 'A' else B(t)
print(1 if t == s else 0)