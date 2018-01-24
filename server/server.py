import asyncio
import websockets

async def setup_websocket(websocket, path):
    name = await websocket.recv()
    print('{0}'.format(name))

start_server = websockets.serve(setup_websocket, 'localhost', 3344)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
