import xmlrpc.client

# Menghubungkan ke server RPC yang berjalan di localhost:8000
server_url = 'http://localhost:8000'
server = xmlrpc.client.ServerProxy(server_url)

# Meminta bilangan prima hingga batas tertentu (misalnya 11)
batas = 11
prima_list = server.rpc_prima(batas)

print(f"Bilangan prima hingga {batas}: {prima_list}")