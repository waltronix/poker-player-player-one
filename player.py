import sys

class Player:
    VERSION = "PlayerOne v1"

    def betRequest(self, game_state):
        sys.stderr.writelines("player one")
        return 5

    def showdown(self, game_state):
        sys.stderr.writelines("player one")
        sys.stderr.writelines(game_state)
