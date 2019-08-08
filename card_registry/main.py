from sanic import Sanic, response
import motor.motor_asyncio
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
    app.Cards = app.codeMems['cards']

@app.route("/get_cards")
async def get_cards(request):
    return response.json({"route": "unimplemented"})

@app.route("/review_cards")
async def review_cards(request):
    return response.json({"route": "unimplemented"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, Debug=True)
