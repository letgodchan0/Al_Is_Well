n = int(input())    #숫자 카드의 개수
tmp = {}
cards = []
for _ in range(n):  #카드와 카드의 개수 딕셔너리에 저장
    card = int(input()) 
    tmp[card] = tmp.get(card, 0) + 1

for key in tmp:
    cards.append((key, tmp[key]))

cards.sort(key=lambda x: x[0])  #카드의 번호로 오름차순 정렬
cards.sort(key=lambda x: x[1], reverse=True)  #카드의 개수로 내림차순 정렬

print(cards[0][0])  #가장 많이 가지고 있는 정수