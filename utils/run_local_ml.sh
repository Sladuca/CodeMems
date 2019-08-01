docker run --rm -p 27017:27017 mongo --name mongo_data
docker run --rm -p 8000:8000 data_pipeline --name data_pipeline
docker run --rm -p 8001:8000 scheduler --name scheduler
