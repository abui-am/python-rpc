
FROM python:3.9-slim

COPY server.py /app/server.py

WORKDIR /app

EXPOSE 8000

CMD ["python", "server.py"]