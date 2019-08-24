from sanic import Sanic, response

import asyncio
import uvloop

import motor.motor_asyncio
from pymongo import ReplaceOne

import aio_pika
from aio_pika import DeliveryMode, Message

#from sanic_cors import CORS, cross_origin
# make sure asyncio uses uvloop too
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()

# # allow CORS for testing
# CORS(app, automatic_options=True)

# middleware
@app.middleware('request')
async def print_request(request):
    print(request.path)
    print(request.json)

##### rabbit stuff #####

async def produce_hello(app):
    channel = await app.rabbit.channel()
    await channel.set_qos(prefetch_count=1)
    exchange = await channel.declare_exchange(
        'hello',
        aio_pika.ExchangeType.DIRECT
    )
    message_body = b'Hello world!'
    message = Message(
        message_body
    )
    while True:
        await exchange.publish(message, routing_key='hello')
        # print(' [x] sent %r' % message)
        await asyncio.sleep(5)

##### setup and cleanup #####

@app.listener('before_server_start')
async def setup_mongo(app, loop):
    # set up database connections
    app.mongoClient = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017,
        io_loop=loop)
    app.mongo = app.mongoClient['CardRegistry']
    app.notes = app.mongo['cards']

@app.listener('before_server_start')
async def setup_rabbit(app, loop):
    app.rabbit = await aio_pika.connect_robust(
        'amqp://guest:guest@rabbit/', loop=loop
    )
    app.hellos = []
    app.add_task(produce_hello)

##### main functionality #####

@app.route('/add_notes', methods=['POST'])
async def add_notes(request):
    data = request.json
    requests = []
    for document in data:
        # aggregate bulk add replace upsert; identical documents get overwritten
        requests.append(ReplaceOne(document, document, upsert=True))
    res = await app.notes.bulk_write(requests, ordered=False)
    return response.json(
        {
            'message': 'inserted %d, replaced %d' %
            (res.inserted_count, res.modified_count)
        },
        status=200)

@app.route('/delete_notes')
async def delete_notes(request):
    return response.json({'route': 'unimplemented'})

@app.route('/hello')
async def show_hellos(request):
    return response.json(app.hellos)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, Debug=True)
