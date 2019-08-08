from sanic import Sanic, response
import motor.motor_asyncio
from pymongo import ReplaceOne
#from sanic_cors import CORS, cross_origin

app = Sanic()
#CORS(app, automatic_options=True)

# print requests
@app.middleware('request')
async def print_request(request):
    print(request.path)
    print(request.json)

@app.listener("before_server_start")
async def setup_db(app, loop):
    app.mongoClient = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017,
        io_loop=loop)
    app.codeMems = app.mongoClient['codeMemsNotes']
    app.Decks = app.codeMems['decks']
    app.Notes = app.codeMems['notes']
    app.Cards = app.codeMems['cards']


@app.route("/add_notes", methods=["POST"])
async def add_notes(request):
    data = request.json
    requests = []
    for document in data:
        # aggregate bulk add replace upsert; identical documents get overwritten
        requests.append(ReplaceOne(document, document, upsert=True))
    res = await app.Notes.bulk_write(requests, ordered=False)
    return response.json(
        {
            "message": "inserted %d, replaced %d" %
            (res.inserted_count, res.modified_count)
        },
        status=200)

@app.route("/delete_notes")
async def delete_notes(request):
    return response.json({"route": "unimplemented"})

@app.route("/add_cards")
async def add_cards(request):
    return response.json({"route": "unimplemented"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, Debug=True)
