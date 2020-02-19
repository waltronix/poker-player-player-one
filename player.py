import sys
import random


class Player:
    VERSION = "Bot: Always Raise"
    PLAYER_NAME = 'Player One'

    def __init__(self, game_state):
        self.game_state = game_state

    def log(self, message):
        sys.stderr.writelines('**********************')
        sys.stderr.writelines(message)

    def betRequest(self):
        self.log(self.game_state)
        self.log(self.get_our_player())

        player = self.get_our_player()
        amount = self.game_state['current_buy_in'] - player['bet'] + self.game_state['minimum_raise']
        return amount

    def showdown(self):
        self.log('showdown')
        self.log(self.game_state)

    def get_our_player(self):
        """ Find our player """
        for player in self.game_state['players']:
            if player['name'] == self.PLAYER_NAME:
                return player
        return None
