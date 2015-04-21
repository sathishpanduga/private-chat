import tornado.websocket


class Echo(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.write_message(message)