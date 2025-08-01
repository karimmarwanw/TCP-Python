import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '1' #add ur host
port = 65432
s.connect((host, port))
print(f"Connected to {host}:{port}")

message = s.recv(1024)

s.close()

print(message.decode('ascii'))