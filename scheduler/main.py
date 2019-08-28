import os

from sanic import Sanic, response

import aio_pika
from aio_pika import IncomingMessage

app = Sanic()

##### rabbit stuff #####

def recieve_hello(message: IncomingMessage):
    with message.process():
        app.hellos.append(message.body)

async def consume_hello(app):
    channel = await app.rabbit.channel()
    # prefetch 1 message from the channel
    await channel.set_qos(prefetch_count=1)
    exchange = await channel.declare_exchange(
        'hello',
        aio_pika.ExchangeType.DIRECT
    )
    # declare a new queue with a unique name exclusive to this client
    queue = await channel.declare_queue(exclusive=True)
    # bind the queue to the exchange such that it recieves all messages sent
    # to that exchange
    await queue.bind(exchange, routing_key='hello')
    # attach callback to event where we recieve a hello from the queue
    await queue.consumer(recieve_hello)

##### setup and cleanup #####

@app.listener('before_server_start')
async def setup_rabbit(app, loop):
    # connection to rabbitMQ
    # probably want to make one for each pub or sub
    app.rabbit = await aio_pika.connect_robust(
        'amqp://gues:guest@{}/'.format(os.eviron['RABBIT_HOSTNAME']), loop=loop
    )
    # list to hold all of the hello's recieved
    app.hellos = []
    app.add_task(consume_hello)

##### main functionality #####

@app.route("/")
async def show_hellos(request):
    return response.json(app.hellos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
