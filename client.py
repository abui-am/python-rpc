import xmlrpc.client

server_url = 'http://localhost:8000'
server = xmlrpc.client.ServerProxy(server_url)

limit = 11
prima_list = server.rpc_prima(limit)

print(f"Bilangan prima hingga {limit}: {prima_list}")