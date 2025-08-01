import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP

# host = '' #add ur host
port = 65432
s.bind((host, port))
s.listen(3)
print(f"Server is listening on {host}:{port}")

while True:
    connection, address = s.accept()
    print(f"Connected {address}")

    message = 'Hi!'
    connection.send(message.encode())

    connection.close()