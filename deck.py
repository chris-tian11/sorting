from card import card
import random
class deck:
    def __init__(self):
        self.deck = []
        for i in range(1, 14):
            self.deck.append(card(i, "hearts"))
        for i in range(1, 14):
            self.deck.append(card(i, "diamonds"))
        for i in range(1, 14):
            self.deck.append(card(i, "spades"))
        for i in range(1, 14):
            self.deck.append(card(i, "clubs"))
    def shuffle(self):
        for i in range(52):
            self.deck[i], self.deck[random.randint(0,51)] = self.deck[random.randint(0,51)], self.deck[i]