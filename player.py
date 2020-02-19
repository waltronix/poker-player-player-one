import sys
import random


class Card:
    def __init__(self, rank, suit=None):
        if isinstance(rank, dict):
            self.rank = rank['rank']
            self.suit = rank['suit']
        else:
            self.rank = rank
            self.suit = suit

    def equal_rank(self, other):
        return self.rank == other.rank


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def has_two_pair(self):
        for card in self.cards:
            for other in self.cards:
                if card != other and card.equal_rank(other):
                    return True
        return False


class Player:
    VERSION = 'Bot: only raise on pair'
    PLAYER_NAME = 'Player One'

    def __init__(self, game_state):
        self.game_state = game_state

    def log(self, message):
        sys.stderr.writelines('**********************\n')
        sys.stderr.writelines(str(message) + '\n')

    def betRequest(self):
        player = self.get_our_player()
        hand = Hand()
        for card in player['hole_cards']:
            hand.add_card(Card(card))

        self.log('has_two_pairs: %s' % (hand.has_two_pair()))

        amount = (
            self.game_state['current_buy_in']
            - player['bet']
        )

        if hand.has_two_pair():
            amount += self.game_state['minimum_raise']

        return amount

    def showdown(self):
        self.log('showdown')
        self.log(self.game_state)

    def get_our_player(self):
        ''' Find our player '''
        for player in self.game_state['players']:
            if player['name'] == self.PLAYER_NAME:
                return player
        return None
