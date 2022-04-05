import socket
s=socket.socket()
s.bind(('localhost',4444))
name=input("Enter name:")
s.listen(5)
conn,addr=s.accept()
print("Connection established with",addr)
client=(conn.recv(1024)).decode()
print(client+" has connected")
conn.send(name.encode())
while True:
    message=input("Name:")
    if message.lower()=='bye':
        conn.send(message.encode())
        break    
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    if message.lower()=='bye':
        break 
    print(client+' : '+message)
    
