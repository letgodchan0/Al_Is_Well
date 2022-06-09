N = int(input())
deck = dict()
for i in range(N):
    card = input()
    if card in deck:
        deck[card] += 1
    else:
        deck[card] = 1

result, result_num = deck.popitem()
for i in deck:
    if deck[i] > result_num:
        result = i
        result_num = deck[i]
    elif deck[i] == result_num:
        if i < result:
            result = i

print(result)

# 틀렸습니다.