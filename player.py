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

    def get_full_score(self):
        if self.has_one_pair():
            return 8
        elif self.has_three_of_a_kind():
            return 6
        elif self.has_flush():
            return 4
        else:
            return 9

    def __get_ranks(self):
        ranks = dict()
        for card in self.cards:
            ranks[card.rank] = ranks.get(card.rank, 0) + 1
        return ranks

    def has_one_pair(self):
        for rank, amount in self.__get_ranks():
            if amount >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        for rank, amount in self.__get_ranks():
            if amount >= 3:
                return True
        return False

    def has_straight(self):
        ranks = [Card.RANK_INDEX[rank] for rank, count in self.__get_ranks() if count > 0]

    def has_flush(self):
        counters = dict()
        for card in self.cards:
            counters[card.suit] = counters.get(card.suit, 0) + 1
            if counters[card.suit] >= 5:
                return True
        return False

class Player:
    VERSION = 'Bot: Score (with round)'
    PLAYER_NAME = 'Player One'

    def __init__(self, game_state):
        self.game_state = game_state

    def log(self, message):
        sys.stderr.writelines('**********************\n')
        sys.stderr.writelines(str(message) + '\n')

    def betRequest(self):
        try:
            player = self.get_our_player()
            hand = Hand()
            for card in player['hole_cards']:
                hand.add_card(Card(card))
            for card in self.game_state['community_cards']:
                hand.add_card(Card(card))

            amount = self.game_state['current_buy_in'] - player['bet']
            score = hand.get_hand_score()

            if self.game_state['community_cards']:
                card_score = hand.get_full_score()
                score = min(score, card_score)

            round = self.game_state['round']
            round_sq = (round * round) + 1

            if score == 1:
                amount += self.game_state['minimum_raise'] * 10
            elif score < 3:
                amount += self.game_state['minimum_raise'] * round_sq
            elif score <= 5:
                amount += self.game_state['minimum_raise']
            else:
                amount = 0

            return amount
        except:
            self.log('ERROR')
            import traceback
            traceback.print_exc(file=sys.stderr)
            return 0

    def showdown(self):
        self.log('showdown')
        self.log(self.game_state)

    def get_our_player(self):
        ''' Find our player '''
        for player in self.game_state['players']:
            if player['name'] == self.PLAYER_NAME:
                return player
        return None
