import socket


__SOCKET_HOST = 'localhost'
__SOCKET_PORT = 8001
__SOCKET_BUFFER = 1024


client = socket.socket()
client.connect((__SOCKET_HOST, __SOCKET_PORT))
print(f'starting client')

while True:
    msg_to_send = input('message to send: ')
    # sends message to server
    client.send(msg_to_send.encode())
    # receives what the socket server sends
    msg_received = client.recv(__SOCKET_BUFFER)
    print(f'message from server: {msg_received.decode()}')

client.close()
