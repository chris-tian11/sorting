from card import card
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