from Cards import Card, Deck, Hand
import unittest


class TestCard(unittest.TestCase):
    # "Test cases specific to the Card class"
    # def test_init(self):
    #     pass
    def test_repr(self):
        card_to_test = Card(3, "clubs")
        assert "Card(3 of clubs)" == repr(card_to_test)


# other tests
class TestDeck(unittest.TestCase):
    """Tests for the deck"""

    def test_for_52_cards(self):
        """Testing for expected total of 52 cards"""
        deck = Deck()
        assert len(deck.card_list) == 52

    def test_for_unusual_amount_of_cards(self):
        deck2 = Deck([2, 1], ["clubs", "spades"])
        assert len(deck2.card_list) == 2


class TestHand(unittest.TestCase):
    # your tests here
    pass


# class TestSort(unittest.TestCase):
#     """Tests for sorted deck"""

#     deck = Deck()
#     assert

unittest.main()  # Runs all tests above
