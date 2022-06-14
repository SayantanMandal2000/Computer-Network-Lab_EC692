import socket
s=socket.socket()
s.connect(('localhost',4444))
while True:
    op=input("Enter operator: ")
    s.send(op.encode())
    if op.lower()=='exit':
        print("Exiting..")
        break
    op1=input("Operand1: ")
    s.send(op1.encode())
    op2=input("Operand2: ")
    s.send(op2.encode())
    ans=(s.recv(1024)).decode()
    print("Answer: ")
    print(ans)
    