import sys


class Player:
    VERSION = "bet 4"

    def betRequest(self, game_state):
        return 4

    def showdown(self, game_state):
        sys.stderr.writelines("player one")
        sys.stderr.writelines(game_state)
