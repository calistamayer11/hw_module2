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


class TestHand(unittest.TestCase):
    # your tests here
    pass


unittest.main()  # Runs all tests above
