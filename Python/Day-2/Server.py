import time
import socket
current_time=time.ctime(time.time())
s=socket.socket()
s.bind(('localhost',4444))
s.listen(5)
print("Waiting for the client......")
while True:
    conn,addr=s.accept()
    print("Connect with client:",addr)
    print("Current time send to client:",current_time)
    conn.sendall(bytes(current_time,'Utf-8'))