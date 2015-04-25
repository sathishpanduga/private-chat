import json

import tornado.websocket

from tornado_app.models import add_message


class Broadcaster(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        print(type(self))
        self.clients.append(self)

    def broadcast(self, message):
        for client in self.clients:
            client.write_message(message)


class MessageHandler(Broadcaster):
    def on_message(self, message):
        print("got: "+message)
        message = json.loads(message)
        created = add_message(**message)
        self.broadcast("{0} [{1}]: {2}".format(
            created.strftime('%H:%M:%S'), message["sender"], message["message"]
        ))