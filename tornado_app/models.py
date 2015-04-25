import datetime
import sqlite3


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
