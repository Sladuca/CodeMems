from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/echo")
async def echo(request):
    return json({"recieved": True, "data": request.json})

@app.route("/upsert_notes")
async def upsert_notes(request):
    return json({"route": "unimplemented"})

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
