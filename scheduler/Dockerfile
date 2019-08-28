FROM python
COPY . /api
RUN pip install sanic aio_pika
EXPOSE 8000
CMD python /api/main.py
