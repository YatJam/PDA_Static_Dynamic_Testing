import unittest
from src.card_game import CardGame
from src.card import Card


class TestCardGame(unittest.TestCase):
  
    
    def setUp(self):
        self.card = Card("Spades", 1)
        self.card1 = Card("Hearts", 4)
        self.card2 = Card("Clubs", 7)
        self.card3 = Card("Diamonds", 1)
        cards = []
        self.cardGame = CardGame(cards)
        
        
    def test_card_is_not_an_ace(self): 
        self.assertEquals( False, self.cardGame.check_for_ace(self.card1))

    def test_card_is_an_ace(self):
        self.assertEquals( True, self.cardGame.check_for_ace(self.card))

    def test_highest_card_value(self):
        self.assertEquals( self.card2, self.cardGame.highest_card(self.card1, self.card2))

    def test_total_card_value(self):
        cards=[self.card, self.card1, self.card2, self.card3]
        self.assertEquals( "You have a total of 13", self.cardGame.cards_total(cards))