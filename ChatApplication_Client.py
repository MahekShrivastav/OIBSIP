import socket
client = socket.socket()
host = socket.gethostname()
port = 5000
client.connect((host,port))

message = input(">>")
while True:
    client.send(message.encode())
    received = client.recv(1024).decode()
    print(f"server : {received}")
    message = input(">>")