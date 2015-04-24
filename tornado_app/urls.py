from tornado_app import websockets

urlpatterns = [
    (r'/websocket', websockets.MessageHandler),
]