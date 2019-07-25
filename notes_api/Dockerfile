FROM python
COPY . /api
RUN pip install sanic pymongo motor sanic_cors
EXPOSE 8000
CMD python /api/main.py
