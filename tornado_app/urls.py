from tornado_app import websockets

urlpatterns = [
    (r'/messages', websockets.MessageHandler),
    (r'/contacts', websockets.ContactsHandler),
    (r'/contactrequests', websockets.ContactRequestsHandler),
]