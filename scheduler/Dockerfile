FROM python
COPY . /api
RUN pip install sanic aiohttp
EXPOSE 8000
CMD python /api/main.py
