import asyncio 
import websockets 

async def connect_to_server():
    async with  websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(connect_to_server())
