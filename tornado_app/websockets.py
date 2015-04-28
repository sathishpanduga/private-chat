import json
from collections import defaultdict

import tornado.websocket

from tornado_app.models import add_message, add_contact, add_contact_request


clients = defaultdict(list)


class Broadcaster(tornado.websocket.WebSocketHandler):
    def open(self):
        print("open")
        clients[self.name].append(self)

    def broadcast(self, message):
        clients[self.name] = [client for client in clients[self.name] if client.ws_connection is not None]
        for client in clients[self.name]:
            client.write_message(message)

    def close(self):
        clients[self.name].remove(self)
        print("closed")


class MessageHandler(Broadcaster):
    name = "messages"

    def on_message(self, message):
        print("got: "+message)
        message = json.loads(message)
        created = add_message(**message)
        message["message"] = "{0} [{1}]: {2}".format(
            created.strftime('%H:%M:%S'), message["sender"], message["message"])
        self.broadcast(json.dumps(message))


class ContactsHandler(Broadcaster):
    name = "contacts"

    def on_message(self, message):
        print("got: "+message)
        add_contact(**json.loads(message))
        self.broadcast(message)


class ContactRequestsHandler(Broadcaster):
    name = "contactrequests"

    def on_message(self, message):
        print("got: "+message)
        add_contact_request(**json.loads(message))
        self.broadcast(message)