import socket


__SOCKET_HOST = 'localhost'
__SOCKET_PORT = 8001
__SOCKET_BUFFER = 1024 # max character to receives
__SOCKET_MAX_REQUEST = 5 # max number of request that the socket can receive/handle in queue

server = socket.socket()
# establishes connection
server.bind((__SOCKET_HOST, __SOCKET_PORT))
server.listen(__SOCKET_MAX_REQUEST)
print(f'server is waiting for connections')

# accepts clients request
conn, addr = server.accept()
print(f'New connection established: {addr}')

while True:
    # receives message from client
    msg_received = conn.recv(__SOCKET_BUFFER)
    print(f'message from client: {msg_received.decode()}')

    msg_to_send = input('message to send: ')
    # sends message to client
    conn.send(msg_to_send.encode())

conn.close()
