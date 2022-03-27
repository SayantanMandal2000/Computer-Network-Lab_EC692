import socket
s=socket.socket()
s.connect(('localhost',4444))
data=s.recv(1024)
print(data.decode())