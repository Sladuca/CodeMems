import os

from sanic import Sanic, response

import motor.motor_asyncio
from pymongo import ReplaceOne

import aio_pika
from aio_pika import IncomingMessage

#from sanic_cors import CORS, cross_origin

app = Sanic()
#CORS(app, automatic_options=True)

# middleware
@app.middleware('request')
async def print_request(request):
    print(request.path)
    print(request.json)

##### rabbit stuff #####

def recieve_hello(message: IncomingMessage):
    with message.process():
        app.hellos.append(message.body)

async def consume_hello(app):
    channel = await app.rabbit.channel()
    await channel.set_qos(prefetch_count=1)
    exchange = await channel.declare_exchange(
        'hello',
        aio_pika.ExchangeType.DIRECT
    )
    queue = await channel.declare_queue(exclusive=True)
    await queue.bind(exchange, routing_key='hello')
    await queue.consume(recieve_hello)


##### setup and cleanup #####

@app.listener('before_server_start')
async def setup_mongo(app, loop):
    # set up database connections
    app.mongoClient = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017,
        io_loop=loop)
    app.mongo = app.mongoClient['CardRegistry']
    app.cards = app.mongo['cards']

@app.listener('before_server_start')
async def setup_rabbit(app, loop):
    app.rabbit = await aio_pika.connect_robust(
        'amqp://guest:guest@{}/'.format(os.environ['RABBIT_HOSTNAME']), loop=loop
    )
    app.hellos = []
    app.add_task(consume_hello)

##### main functionality #####

@app.route('/hello')
async def show_hellos(request):
    return response.json(app.hellos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
