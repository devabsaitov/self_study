
import asyncio
import websockets

clients = set()

async def server(websocket, path):
    clients.add(websocket)
    try:
        # msg = asyncio.wait_for(websocket.recv() ,timeout=100 )
        # websockets.broadcast(clients ,msg)
        async for message in websocket:
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)
        print("Client disconnected")


async def start_server():
    async with websockets.serve(server, "10.10.1.239", 8765):
        print("Server started")
        await asyncio.Future()  # Run forever
git remote set-url origin git://github.com/devabsaitov/self_study.git


if __name__ == '__main__':
    asyncio.run(start_server())

