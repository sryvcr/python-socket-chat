import socket


__SOCKET_HOST = 'localhost'
__SOCKET_PORT = 8001
__SOCKET_BUFFER = 1024


client = socket.socket()
client.connect((__SOCKET_HOST, __SOCKET_PORT))


# sends message to server
client.send(f'Hello from client'.encode())
# receives what the socket server sends
msg = client.recv(__SOCKET_BUFFER)
print(msg.decode())
client.close()
