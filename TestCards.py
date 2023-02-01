from Cards import Card, Deck, Hand
import unittest


class TestCard(unittest.TestCase):
    """Test cases specific to the Card class"""

    def test_hand_init(self):
        """Tests init of card class"""
        card_to_test = Card(3, "clubs")
        assert card_to_test.suit == "clubs"
        assert card_to_test.value == 3

    def test_repr(self):
        """Tests repr of card class"""
        card_to_test = Card(3, "clubs")
        assert "Card(3 of clubs)" == repr(card_to_test)

    def test_lt(self):
        """Tests < operator of card class"""
        assert Card(3, "clubs") < Card(1, "spades")

    def test_eq(self):
        """Tests == operator of card class"""
        assert Card(1, "hearts") == Card(1, "hearts")


# other tests
class TestDeck(unittest.TestCase):
    """Tests for the deck"""

    def test_deck_init(self):
        """Tests for init of deck class"""
        deck = Deck()
        deck2 = Deck([2, 1], ["clubs", "spades"])
        assert len(deck.card_list) == 52
        assert len(deck2.card_list) == 2
        assert repr(deck2.card_list) == "[Card(2 of clubs), Card(1 of spades)]"
        assert repr(deck2.suits) == "['clubs', 'spades']"

    def test_deck_repr(self):
        """Tests for repr of deck class"""
        deck = Deck([2, 1], ["clubs", "spades"])
        assert repr(deck) == "Deck: [Card(2 of clubs), Card(1 of spades)]"

    def test_deck_len(self):
        """Tests length method for deck class"""
        deck = Deck([2, 1], ["clubs", "spades"])
        assert len(deck) == 2

    def test_deck_sort(self):
        """Tests the sort method of the deck class by sorthing the card list"""
        deck = Deck([2, 1], ["spades", "clubs"])
        deck.sort()
        assert repr(deck.card_list) == "[Card(1 of clubs), Card(2 of spades)]"

    def test_deck_shuffle(self):
        """Test shuffle method"""
        # highly unlikely to fail, but it is possible if shuffle returns the same ordered deck
        deck = Deck()
        string_repr = repr(deck.card_list)
        deck.shuffle()
        string_repr_shuffle = repr(deck.card_list)
        assert string_repr != string_repr_shuffle

    def test_draw_top(self):
        """Tests draw top method"""
        deck = Deck([2, 1], ["spades", "clubs"])
        one_of_clubs = deck.draw_top()
        assert repr(one_of_clubs) == "Card(1 of clubs)"
        assert len(deck.card_list) == 1


class TestHand(unittest.TestCase):
    """Class for testing the Hand Class methods"""

    # your tests here
    def test_hand_init(self):
        """Tests init for hand class"""
        card1 = Card(3, "clubs")
        card2 = Card(1, "hearts")
        card3 = Card(9, "spades")
        test_hand = Hand([card1, card2, card3])

        assert len(test_hand.card_list) == 3
        assert (
            repr(test_hand.card_list)
            == "[Card(3 of clubs), Card(1 of hearts), Card(9 of spades)]"
        )

    def test_hand_repr(self):
        """Tests repr for hand class"""
        card1 = Card(3, "clubs")
        card2 = Card(1, "hearts")
        card3 = Card(9, "spades")
        test_hand = Hand([card1, card2, card3])
        assert (
            repr(test_hand)
            == "Hand: [Card(3 of clubs), Card(1 of hearts), Card(9 of spades)]"
        )

    def test_hand_len(self):
        """Tests length method for hand class"""
        hand = Hand([Card(1, "clubs"), Card(2, "spades")])
        assert len(hand) == 2

    def test_hand_play(self):
        """Tests play method for hand class"""
        card1 = Card(3, "clubs")
        card2 = Card(1, "hearts")
        card3 = Card(9, "spades")
        test_hand = Hand([card1, card2, card3])

        # method play returns card as well as removing from list
        assert test_hand.play(card1) == card1
        # After playing card1, there should only be card2 and card3 left
        assert repr(test_hand.card_list) == "[Card(1 of hearts), Card(9 of spades)]"


unittest.main()  # Runs all tests above
