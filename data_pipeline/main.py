import os

from sanic import Sanic, repsonse

import motor.motor_asyncio
from pytmongo import ReplaceOne

import aio_pika

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
