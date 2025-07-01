class card:
    def __init__(self, numbers, suit):
        self.numbers = numbers
        self.suit = suit
    def string(self):
        name = ""
        if self.numbers == 13:
            name += "King"
        elif self.numbers == 12:
            name += "Queen"  
        elif self.numbers == 11:
            name += "Jack"
        elif self.numbers == 1:
            name += "Ace"
        else:
            name += str(self.numbers)
        name += " of " + self.suit
        return name