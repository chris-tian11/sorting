from card import card
from deck import deck
deck1 = deck()
deck1.shuffle()
player1 = []
player2 = []

for i in range(26):
    deal1 = deck1.deck[i]
    player1.append(deal1)

for x in range(27, 52):
    deal2 = deck1.deck[x]
    player2.append(deal2)

if player1[0] > player2[0]:
    print("player 1 wins")