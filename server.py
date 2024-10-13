import xmlrpc.server

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def rpc_prima(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
print("Server is running on port 8000...")

# Mendaftarkan fungsi pada server
server.register_function(rpc_prima, 'rpc_prima')

# Menjalankan server
server.serve_forever()