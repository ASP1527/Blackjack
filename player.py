class player:
    def __init__(self, hand, points):
        self.hand = hand
        self.points = points
    
    def hit(self, deck):
        card = deck[0]
        deck.remove(card)
        self.hand.append(card)
        splitCard = card.split(" ")
        value = splitCard[1]
        if value == "K" or value == "Q" or value == "J":
            self.points += 10
        elif value == "A":
            if self.points + 11 > 21:
                self.points += 1
            else:
                self.points += 11
        else:
            value = int(value)
            self.points += value

        return card
    
