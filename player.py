import sys
import random


class Card:
    REDS = ('hearts', 'diamonds')
    BLACKS = ('clubs', 'spades')

    RANK_INDEX = {
        "A": 0,
        "K": 1,
        "Q": 2,
        "J": 3,
        "10": 4,
        "9": 5,
        "8": 6,
        "7": 7,
        "6": 8,
        "5": 9,
        "4": 10,
        "3": 11,
        "2": 12,
    }

    def __init__(self, rank, suit=None):
        if isinstance(rank, dict):
            self.rank = rank['rank']
            self.suit = rank['suit']
        else:
            self.rank = rank
            self.suit = suit

    def get_rank_index(self):
        return self.RANK_INDEX[self.rank]

    def equal_rank(self, other):
        return self.rank == other.rank


class Hand:
    MATRIX = (
        (1,1,2,2,3,5,5,5,5,5,5,5,5),
        (2,1,2,3,4,6,7,7,7,7,7,7,7),
        (3,4,1,3,4,5,7,9,9,9,9,9,9),
        (4,5,5,1,3,4,6,8,9,9,9,9,9),
        (6,6,6,5,2,4,5,7,9,9,9,9,9),
        (8,8,8,7,7,3,4,5,8,9,9,9,9),
        (9,9,9,8,8,7,4,5,6,8,9,9,9),
        (9,9,9,9,9,9,8,5,5,6,8,9,9),
        (9,9,9,9,9,9,9,8,6,7,7,9,9),
        (9,9,9,9,9,9,9,9,8,6,6,7,9),
        (9,9,9,9,9,9,9,9,9,8,7,7,8),
        (9,9,9,9,9,9,9,9,9,9,9,7,8),
        (9,9,9,9,9,9,9,9,9,9,9,9,7),
    )

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

    def get_hand_score(self):
        index_0 = self.cards[0].get_rank_index()
        index_1 = self.cards[1].get_rank_index()
        if self.cards[0].suit == self.cards[1].suit:
            row = min(index_0, index_1)
            col = max(index_0, index_1)
        else:
            row = max(index_0, index_1)
            col = min(index_0, index_1)
        return self.MATRIX[row][col]

class Player:
    VERSION = 'Bot: score (full matrix)'
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

        score = hand.get_hand_score()

        if score < 5:
            amount += self.game_state['minimum_raise']
        elif hand.get_hand_score() > 8:
            amount = 0

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
