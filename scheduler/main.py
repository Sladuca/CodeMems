from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/hello")
async def hello(request):
    return json({"hello": "world"})

@app.route("/upsert_notes")
async def upsert_notes(request):
    return json({"route": "unimplemented"})

@app.route("/delete_notes")
async def delete_notes(request):
    return json({"route": "unimplemented"})

@app.route("/get_reviews")
async def get_reviews(request):
    return json({"route": "unimplemented"})

@app.route("/update_reviews")
async def update_reviews(request):
    return json({"route": "unimplemented"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
