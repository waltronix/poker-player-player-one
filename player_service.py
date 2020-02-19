import os
import time
import json
from bottle import route, run, request
from player import Player


HOST_NAME = "0.0.0.0"
PORT_NUMBER = int(os.environ.get("PORT", 0)) or 9000


@route('/', method='POST')
def handler():
    action = request.forms.get('action')
    if action == 'check':
        return 'check'
    elif action == 'version':
        return Player.VERSION
    elif action == 'bet_request':
        state = json.loads(request.forms.get('game_state', '{}'))
        return Player().betRequest(state)
    elif action == 'showdown':
        state = json.loads(request.forms.get('game_state', '{}'))
        return Player().showdown(state)
    else:
        return 'Fuck you!'


if __name__ == '__main__':
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        run(host=HOST_NAME, port=PORT_NUMBER, debug=True)
    except KeyboardInterrupt:
        pass
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
