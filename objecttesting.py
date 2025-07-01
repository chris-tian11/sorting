from card import card
from deck import deck

deck1 = deck()

for i in range(52):
    print(deck1.deck[i].string())