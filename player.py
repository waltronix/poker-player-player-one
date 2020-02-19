import sys


class Player:
    VERSION = "more logging"

    def betRequest(self, game_state):
        sys.stderr.writelines("player one - bet request")
        return 4

    def showdown(self, game_state):
        sys.stderr.writelines("player one")
        sys.stderr.writelines(game_state)
