
FROM python:3.9-slim

COPY server.py /app/server.py

WORKDIR /app

# Expose port untuk server RPC
EXPOSE 8000

# Menjalankan server sebagai default command
CMD ["python", "server.py"]