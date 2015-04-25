import json

import tornado.websocket

from tornado_app.models import add_message


class MessageHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        print(type(self))
        self.clients.append(self)

    def on_message(self, message):
        message = json.loads(message)
        created = add_message(**message)
        for client in self.clients:
            client.write_message("{0} [{1}]: {2}".format(
                created.strftime('%H:%M:%S'), message["sender"], message["message"]
            ))