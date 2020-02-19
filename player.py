import sys
import random


class Player:
    VERSION = "bet 4"
    PLAYER_NAME = 'Player One'

    def __init__(self, game_state):
        self.game_state = game_state

    def log(self, message):
        sys.stderr.writelines('**********************')
        sys.stderr.writelines(message)

    def betRequest(self):
        self.log(self.game_state)
        self.log(self.get_our_player())
        return 4

    def showdown(self):
        self.log('showdown')
        self.log(self.game_state)

    def get_our_player(self):
        """ Find our player """
        for player in self.game_state['players']:
            if player['name'] == self.PLAYER_NAME:
                return player
        return None
