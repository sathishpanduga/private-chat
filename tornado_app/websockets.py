import json
import sqlite3
import datetime

import tornado.websocket


conn = sqlite3.connect("db.sqlite3")


def get_user_id(username):
    return conn.execute("SELECT id FROM auth_user WHERE username = :username",
                        {"username": username}).fetchone()[0]


def add_message(sender, receiver, message):
    created = datetime.datetime.now()
    conn.execute(
        "INSERT INTO private_chat_message (sender_id, receiver_id, message, created)"
        " VALUES (:sender_id, :receiver_id, :message, :created)",
        {
            "sender_id": get_user_id(sender),
            "receiver_id": get_user_id(receiver),
            "message": message,
            "created": created,
        }
    )
    conn.commit()
    return created


class MessageHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        self.clients.append(self)

    def on_message(self, message):
        message = json.loads(message)
        created = add_message(**message)
        for client in self.clients:
            client.write_message("{0} [{1}]: {2}".format(
                created.strftime('%H:%M:%S'), message["sender"], message["message"]
            ))