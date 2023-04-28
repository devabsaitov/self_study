# import asyncio
# import websockets
#
#
# async def client():
#     async with websockets.connect("ws://10.10.1.239:8765") as websocket:
#         msg = input('<<<')
#         await websocket.send(msg)
#         response = await websocket.recv()
#         print(f'>>>{response}')
#
# async def start_client():
#     while True:
#         await client()
#         await asyncio.sleep(1)
#
#
# if __name__ == '__main__':
#     asyncio.run(start_client())
import asyncio
import websockets


async def client():
    async with websockets.connect("ws://10.10.1.239:8765") as websocket:
        msg = input('<<<')
        await websocket.send(msg)
        while (msg:=await websocket.recv()):
            print(f'>>>{msg}')
            msg = input('<<<')
            await websocket.send(msg)

        # message = await asyncio.wait_for(, timeout=100)

async def start_client():
    while True:
        await client()
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(start_client())

