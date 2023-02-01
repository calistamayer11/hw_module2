from random import shuffle

# key function for sorting
def sort_card(card_obj):
    """key function for sort in Deck class"""
    return card_obj.suit, card_obj.value


# create default values and suits for Deck Class
default_values = []
default_suits = []
for suit in ["clubs", "diamonds", "hearts", "spades"]:
    for value in list(range(1, 14)):
        default_values.append(value)
        default_suits.append(suit)


class Deck:
    """A class that initiates a deck of cards, a card list, a sort method and a shuffle method"""

    def __init__(self, values=default_values, suits=default_suits):
        """Initializes the deck class"""
        self.suits = suits
        self.values = values
        self.card_list = []

        # length of lists suits and values should be the same
        for index in range(len(suits)):
            self.card_list.append(Card(values[index], suits[index]))

    def __repr__(self):
        """Magic method for repr"""
        return f"Deck: {self.card_list}"

    def __len__(self):
        """Magic method for length method"""
        return len(self.card_list)

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
    """A class that creates a card object"""

    def __init__(self, value, suit):
        """Initializes the card class"""
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

    def __eq__(self, card):
        """Magic method for equal method"""
        if self.suit == card.suit and self.value == card.value:
            return True
        else:
            return False


class Hand(Deck):
    """A class that initiates a hand of cards and has a card list and a play method"""

    def __init__(self, card_list):
        """Initializes the hand class"""
        self.card_list = card_list

    def __repr__(self):
        """Magic method for repr"""
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
