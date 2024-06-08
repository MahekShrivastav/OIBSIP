import socket
server  = socket.socket()
server.bind(("",5000))
server.listen()
connection,address = server.accept()
print(f"New connection from : {address}")

while True:
    received = connection.recv(1024).decode()
    print(f"client : {received}")
    message = input(">>")
    connection.send(message.encode())