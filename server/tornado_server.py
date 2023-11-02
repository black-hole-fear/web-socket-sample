import tornado.web
import tornado.websocket 
import tornado.ioloop 

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Websocket opened")

    def on_message(self, message):
        self.write_message(f"You said: {message}")

    def on_close(self):
        print("Websocket closed")

app = tornado.web.Application([(r'/ws', WebSocketHandler)])

if __name__ == "__main__":
    app.listen(8765)
    tornado.ioloop.IOLoop.current().start()