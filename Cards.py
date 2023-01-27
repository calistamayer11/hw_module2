class Deck:
    def __init__(self):
        self.suits = ["spades", "hearts", "diamonds", "clubs"]
        self.values = list(range(1, 14))
        self.card_list = []
        for suit in self.suits:
            for value in self.values:
                self.card_list.append(Card(value, suit))


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"Card({self.value} of {self.suit})"


class Hand(Deck):
    def __init__(self, card_list):
        self.card_list = card_list


# deck = Deck()
# print(len(deck.card_list))
# print(deck.card_list[48].suit)
# print(deck.card_list[48].value)
