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


def add_contact(accepter, requester):
    accepter_id = get_user_id(accepter)
    requester_id = get_user_id(requester)
    print("{0}({1}) accepted request from {2}({3})".format(accepter, accepter_id, requester, requester_id))
    conn.execute(
        "INSERT INTO private_chat_contact (accepter_id, requester_id)"
        " VALUES (:accepter_id, :requester_id)",
        {
            "accepter_id": accepter_id,
            "requester_id": requester_id,
        }
    )
    conn.execute(
        "DELETE FROM private_chat_contactrequest"
        " WHERE accepter_id = :accepter_id"
        " AND requester_id = :requester_id",
        {
            "accepter_id": accepter_id,
            "requester_id": requester_id,
        }
    )
    conn.commit()