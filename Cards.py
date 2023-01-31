from random import shuffle


def sort_card(card_obj):
    """key function for sort in Deck class"""
    return card_obj.suit, card_obj.value


class Deck:
    def __init__(self, values=None, suits=None):
        # self.suits = ["clubs", "diamonds", "hearts", "spades"]
        self.suits = suits
        # self.values = list(range(1, 14))
        self.values = values
        self.card_list = []
        # if lists are None, create default deck of 52 cards
        if values == None and suits == None:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                for value in list(range(1, 14)):
                    self.card_list.append(Card(value, suit))
        else:
            # length of lists suits and values should be the same
            for index in range(len(suits)):
                self.card_list.append(Card(values[index], suits[index]))

    def __repr__(self):
        return f"Deck: {self.card_list}"

    def sort(self):
        """run sorted, key function returns tuple in order that sort is wanted -> suit then value"""
        self.card_list = sorted(self.card_list, key=sort_card)

    def shuffle(self):
        """Imported shuffle from random to shuffle list"""
        shuffle(self.card_list)

    def draw_top(self):
        """Use pop method to remove last card in list and return card object"""
        return self.card_list.pop()


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Returns value and suit as a string"""
        return f"Card({self.value} of {self.suit})"

    def __lt__(self, card):
        """Sort by suit first, then sort by value. Will only sort by value if the suits are the same."""
        if self.suit == card.suit:
            return self.value < card.value
        else:
            return self.suit < card.suit


# print(Card(1, "clubs") < Card(2, "clubs"))
# print(Card(2, "clubs") < Card(1, "clubs"))
# print(Card(1, "spades") < Card(1, "clubs"))


class Hand(Deck):
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        return f"Hand: {self.card_list}"

    def play(self, card):
        """
        Removes card object from card_list and returns card object
        Raises error if card isn't in list
        """
        if card in self.card_list:
            self.card_list.remove(card)
            return card
        else:
            raise Exception(
                f"Attempt to play {card} that is not in Hand: {self.card_list}"
            )


# deck = Deck()
# print(len(deck.card_list))
# print(deck.card_list[48].suit)
# print(deck.card_list[48].value)
two_of_spades = Card(2, "spades")
deck2 = Deck([10, 2, 5, 1], ["hearts", "spades", "clubs", "clubs"])
hand = Hand([Card(10, "hearts"), two_of_spades])

print(f"{deck2=}")
# deck2.sort()
# print(f"{deck2=}")
# print(deck2.draw_top())
# print(deck2.card_list)
card = hand.play(two_of_spades)
print(f"{card=}")
print(hand.play(two_of_spades))
print(hand)
print(hand.play(two_of_spades))
