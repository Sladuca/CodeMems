FROM python
COPY . /api
RUN pip install sanic pymongo motor sanic_cors aio_pika
EXPOSE 8000
CMD python /api/main.py
