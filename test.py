from player import Player
import json

if __name__ == '__main__':
    with open('test.json', 'r') as file:
        state = json.loads(file.read())
    print(Player(state).betRequest())
