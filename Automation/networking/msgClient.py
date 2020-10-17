import socket

"""

A basic echo client for Socket practice

"""

# Host and port used by server
HOST = '127.0.0.1'
PORT = 55555

DATA_BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while 1:
        s.sendall(bytes(input("Send: "), encoding='utf-8'))
        data = s.recv(DATA_BUFFER_SIZE)
        print("Received:", str(data, encoding='utf-8'))  # Return the canonical string representation of the object.

