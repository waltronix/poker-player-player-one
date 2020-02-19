import sys

class Player:
    VERSION = "bet 5"

    def betRequest(self, game_state):
        return 5

    def showdown(self, game_state):
        sys.stderr.write(game_state)
