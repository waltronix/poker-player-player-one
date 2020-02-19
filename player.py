import sys
import random


class Player:
    VERSION = "bet 4"

    def __init__(self, game_state):
        self.game_state = game_state

    def betRequest(self):
        sys.stderr.writelines(self.game_state)
        return 4

    def showdown(self):
        sys.stderr.writelines("player one")
        sys.stderr.writelines(self.game_state)

    def get_our_player(self):
        """ Find our player """
        pass
