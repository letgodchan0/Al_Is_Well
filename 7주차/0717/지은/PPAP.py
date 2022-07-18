word = input()
ppap = []
for w in word:
    ppap.append(w)
    if ppap[-4:] == ['P', 'P', 'A', 'P']:
        del ppap[-4:]
        ppap.append('P')
print('PPAP' if ppap == ['P', 'P', 'A', 'P'] or ppap == ['P'] else 'NP')    