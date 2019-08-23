FROM python
COPY . /api
RUN pip install pymongo motor sanic aio-pika asyncio
EXPOSE 8000
CMD python /api/main.py
