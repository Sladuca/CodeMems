docker run --rm -p 27017:27017 mongo --name mongo_notes
docker run --rm -p 8000:8000 notes_api --name notes_api
docker run --rm -p 8001:8000 frontend --name frontend
