from sanic import Sanic, response
import motor.motor_asyncio
from pymongo import replaceOne

app = Sanic()

# validate requests
@app.middleware('request')
async def is_valid_request(request):
    # for each route, implement a function that checks validity
    if request.path == "/add_notes":
        print type(request.json)
        return isInstance(request.json, list)
    pass

@app.listener("before_server_start")
async def setup_db(app, loop):
    app.mongoClient = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017,
        io_loop=loop)
    app.Notes = app.mongoClient['Notes']
    app.Cards = app.mongoClient['Cards']

@app.route("/echo")
async def echo(request):
    return json({"recieved": True, "data": request.json})

@app.route("/add_notes", methods=["POST"])
async def add_notes(request):
    data = request.json
    requests = []
    rejected = 0
    for document in data:
        # aggregate bulk add replace upsert; identical documents get overwritten
        requests.append([replaceOne(data, data, upsert=True)])
    res = await app.Notes.bulk_write(requests, ordered=False)
    return json(
        {
            "message": "inserted %d, replaced %d" %
            (res.inserted_count, res.modified_count)
        },
        status=200)

@app.route("/delete_notes")
async def delete_notes(request):
    return json({"route": "unimplemented"})

@app.route("/get_cards")
async def get_cards(request):
    return json({"route": "unimplemented"})

@app.route("/review_cards")
async def update_cards(request):
    return json({"route": "unimplemented"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
