
FROM python:3.9-slim

COPY server.py /app/server.py
COPY client.py /app/client.py

WORKDIR /app

# Install XMLRPC server dependencies
RUN pip install xmlrpc-server

# Expose port untuk server RPC
EXPOSE 8000

# Menjalankan server sebagai default command
CMD ["python", "server.py"]