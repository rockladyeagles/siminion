
class Card():
    """
    The ultimate base class of the entire Card hierarchy.
    """
    def __init__(self, deck):
        self.deck = deck
        self.keywords = set()

    def VPs(self):
        '''
        Returns the number of Victory Points this card is worth at end of
        game.
        '''
        return 0

    @classmethod
    def cost(self):
        '''
        Returns the number of coins required to buy this card.
        '''
        return 0

    def play(self):
        '''
        The default "play" behavior is simply to move the card from the hand to
        the play area.
        '''
        self.deck.playArea |= { self }
        self.deck.hand -= { self }
