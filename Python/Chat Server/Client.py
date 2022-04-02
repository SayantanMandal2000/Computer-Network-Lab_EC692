import socket
name=input("Enter friend's name:")
s=socket.socket()
s.connect(('localhost',4444))
s.send(name.encode())
server_name=s.recv(1024)
server_name=server_name.decode()
print(server_name+" has joined....")
while True:
    message=(s.recv(1024)).decode()
    print(server_name+" : "+message)
    if message.lower()=='eye':
        break
    message=input("Name:")
    if message.lower()=='eye':
        s.send(message.encode())
        break
    s.send(message.encode())
    