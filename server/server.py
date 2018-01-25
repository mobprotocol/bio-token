import asyncio
import websockets

async def setup_websocket(websocket, path):
    data = await websocket.recv()
    print('{0}'.format(data))
    processed_data = await process_data(data)
    await websocket.send(processed_data)

async def process_data(data):
    return data + ' hey this is the server responding'

start_server = websockets.serve(setup_websocket, 'localhost', 3344)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
