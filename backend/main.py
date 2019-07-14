from sanic import Sanic, response
import motor.motor_asyncio
from pymongo import ReplaceOne
from sanic_cors import CORS, cross_origin

app = Sanic()
CORS(app, automatic_options=True)

# print requests
@app.middleware('request')
async def print_request(request):
    print(request.path)
    print(request.json)

# # allow cors CORS for now
# @app.middleware('request')
# async def allow_cors(request):
#     if request.method == "OPTIONS":
#         return response.json(
#         {"allow": "CORS"},
#         headers={"Access-Control-Allow-Methods": ["POST", "GET", "OPTIONS"]},
#         status=200,
#         )

@app.listener("before_server_start")
async def setup_db(app, loop):
    app.mongoClient = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017,
        io_loop=loop)
    app.codeMems = app.mongoClient['codeMems']
    app.Notes = app.codeMems['Notes']
    app.Cards = app.codeMems['Cards']

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
    return json({"route": "unimplemented"})

@app.route("/get_cards")
async def get_cards(request):
    return json({"route": "unimplemented"})

@app.route("/review_cards")
async def update_cards(request):
    return json({"route": "unimplemented"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
