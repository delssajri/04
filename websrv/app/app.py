#!/usr/bin/python


import json
import traceback

import tornado.ioloop
import tornado.web
import tornado.websocket

import couchdb


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class WebSocket(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        try:
            query = None
            try:
                query = json.loads(message)
            except:
                print traceback.format_exc()
                self.ws_connection.write_message(
                    '{"status": 400, "reason": "Bad request"}')
                return
            self.dispatch(query)
        except:
            print traceback.format_exc()
            self.ws_connection.write_message(
                '{"status": 503, "reason": "Internal server error"}')

    def dispatch(self, query):
        if not query.has_key('action'):
            self.ws_connection.write_message('{"status": 400, "reason": "Missing action field"}')
            return

        if query['action'] == 'placeOrder':
            self.place_order(query)
            return

        self.ws_connection.write_message(
            '{"status": 404, "reason": "Action {0} not supported"}'.format(query.action))

    def place_order(self, query):
        try:
            owner = query['payment']['owner'].strip()
            number = query['payment']['number'].strip()
            expires_at = query['payment']['expiresAt'].strip()
            cvv = query['payment']['cvv'].strip()
        except:
            print traceback.format_exc()
            self.ws_connection.write_message(
                '{"status": 404, "reason": "Missing payment fields"}')
            return
        try:
            self.verify_number(number)
            self.verify_expires_at(expires_at)
            self.verify_cvv(cvv)
        except:
            print traceback.format_exc()
            self.ws_connection.write_message(
                '{"status": 404, "reason": "Incorrect payment fields"}')
            return
        order = {
            'payment': {
                'owner': owner,
                'number': number,
                'expiresAt': expires_at,
                'cvv': cvv
            }
        }
        print order
        self.application.db.save(order)
        self.ws_connection.write_message(
            '{"status": 200, "reason": "OK"}')

    def verify_number(self, number):
        if len(number) != 16:
            raise ValueError()
        # s = 0
        # for i, n in enumerate(number):
        #     s += int(n) * (1 + i % 2)
        # if s % 10 != 0:
        #     raise ValueError

    def verify_expires_at(self, expires_at):
        if len(expires_at) != 4:
            raise ValueError
        for e in expires_at:
            int(e)

    def verify_cvv(self, cvv):
        if len(cvv) != 3:
            raise ValueError
        for c in cvv:
            int(c)


class Application(tornado.web.Application):
    def __init__(self):
        self.__init_tornado()
        self.__init_db()

    def __init_tornado(self):
        handlers = (
            (r'/', MainHandler),
            (r'/websocket/?', WebSocket),
        )

        tornado.web.Application.__init__(self, handlers)

    def __init_db(self):
        couch = couchdb.Server(url='http://couch:5984/')
        try:
            self.db = couch['payments']
        except:
            self.db = couch.create('payments')


if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
