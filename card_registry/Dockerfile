FROM python
RUN pip install pymongo motor sanic aio-pika
COPY . /api
EXPOSE 8000
CMD python /api/main.py
