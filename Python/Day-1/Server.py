import socket
s=socket.socket()
print("Socket is created")
s.bind(('localhost',4444))
s.listen()
print("Waiting for the connection.....")
while True:
    conn,add=s.accept()
    print("Connection with",add)
    conn.send(bytes("Welcome Client",'Utf-8'))