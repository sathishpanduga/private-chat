from tornado_app import websockets

urlpatterns = [
    (r'/messages', websockets.MessageHandler),
]