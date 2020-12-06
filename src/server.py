import socket


__SOCKET_HOST = 'localhost'
__SOCKET_PORT = 8001
__SOCKET_BUFFER = 1024 # max character to receives


server = socket.socket()
# establishes connection
server.bind((__SOCKET_HOST, __SOCKET_PORT))
# set number of request that the socket can receive/ in queue
server.listen(5)


while True:
    # accepts clients request
    conn, addr = server.accept()
    print(f'New connection established: {addr}')

    # receives message from client
    msg = conn.recv(__SOCKET_BUFFER)
    print(msg.decode())

    # sends a default message to client
    conn.send(f'Hello, greetings from server'.encode())
    conn.close()
