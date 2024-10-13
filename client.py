import xmlrpc.client

server_url = 'http://localhost:8000'
server = xmlrpc.client.ServerProxy(server_url)

batas = 11
prima_list = server.rpc_prima(batas)

print(f"Bilangan prima hingga {batas}: {prima_list}")