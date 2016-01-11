#!/usr/bin/python


import json
from websocket import create_connection


def place_order(owner, card_number, expires_at, cvv):
    order = json.dumps({
        'action': 'placeOrder',
        'payment': {
            'owner': owner,
            'number': card_number,
            'expiresAt': expires_at,
            'cvv': cvv
        }
    })
    print 'Opening connection...'
    ws = create_connection("ws://localhost:8888/websocket")
    print 'Sending order...'
    ws.send(order)
    print 'Waiting server response...'
    result = ws.recv()
    print 'Received <{0}>'.format(result)
    ws.close()


if __name__ == "__main__":
    place_order('James Doe', '4042692503974178', '1217', '123')
