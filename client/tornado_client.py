import tornado.websocket
import tornado.ioloop 

class WebSocketClient(tornado.websocket.WebSocketClientConnection):
    async def send_message(self, message):
        await self.write_message(message)

async def connect_to_server():
    url = "ws://localhost:8765/ws"
    client = await tornado.websocket.websocket_connect(url)
    await client.write_message("Hello, there?")
    response = await client.read_message()
    print(f"Received: {response}")

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(connect_to_server)