import socket
c=socket.socket()
c.connect(('localhost',4444))
print(c.recv(1024).decode())