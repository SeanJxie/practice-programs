import socket

HOST = '127.0.0.1'  # "localhost" IPv4 address (loopback)

PORT = 55555  # Anything between 49152 - 65536

DATA_BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Create socket object
    s.bind((HOST, PORT))  # Associate the socket with network and port
    s.listen()  # Listen enables a server to
    connection, address = s.accept()  # Accept connections

    while 1:
        with connection:  # Automatically closes socket at end of block
            print('Connected by:', address)

            while True:
                try:
                    data = connection.recv(DATA_BUFFER_SIZE)  # Max number of byte data to send
                    print("Received:", str(data, encoding='utf-8'))

                except (ConnectionResetError, OSError) as e:
                    print(address, "has disconnected")
                    break

                try:
                    connection.sendall(bytes(input("Send: "), encoding='utf-8'))
                except ConnectionResetError:
                    print(address, "has disconnected")
                    break

        break
